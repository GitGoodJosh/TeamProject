import os
import time
import pygame
import pygameClasses
import random

pygame.init()
# need list for pygame height and width (cannot usse two separate numbers)
screensize = (1000, 600)
# if changing bg pic remember to change size to fit 
#TeamGame\TeamProject\Assets\pygameBACKGROUND.png
pygame.display.set_mode(screensize)
pygame.display.set_caption(" GAME ")
# Image Load Function
def LoadImg(img):
    return pygame.image.load(os.path.join(Asset_dir,img)).convert_alpha()

def FlipImg(img, verticalFlip:bool, horizontalFlip:bool):
    return pygame.transform.flip(img, verticalFlip, horizontalFlip)

# load all images after this line
Asset_dir = os.path.join(os.path.dirname(__file__), 'Assets')
BGimage = LoadImg('pygameBACKGROUND.png')
TANKimage = LoadImg('pygameTANK.png')
FIGHTERimage = LoadImg('pygameFIGHTER.png')
HEALERimage = LoadImg('pygameHEALER.png')
FIGHTERimageAI = FlipImg(FIGHTERimage, True, False)
TANKimageAI = FlipImg(TANKimage, True, False)


screen = pygame.display.get_surface()

# load all images before this line
# ------------------------------------------------- #
def ChooseChar(x, y):
    CharChosen = False
    Char = None
    while CharChosen == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_t:
                    Char =  pygameClasses.character(x, y, 200, 30, 20, TANKimage, True , 0)
                    CharChosen = True
                    
                elif event.key == pygame.K_f:
                    Char = pygameClasses.character(x, y, 150, 50, 10, FIGHTERimage, True , 0)
                    CharChosen = True
    return Char

def show_text( msg, color, x, y ):
    font = pygame.font.SysFont(None, 30)
    text = font.render( msg, True, color)
    screen.blit(text, ( x, y ) )

def refreshScreen():
    CheckAliveAll()

    screen.blit(BGimage, (0,0))
    if playerChar1.alive == True:
        screen.blit(playerChar1.image, (playerChar1.xCoord,playerChar1.yCoord))
        show_text(str(playerChar1.hpCurrent), (0, 0, 255), playerChar1.xCoord + 50, playerChar1.yCoord - 20)

    if playerChar2.alive == True:
        screen.blit(playerChar2.image, (playerChar2.xCoord,playerChar2.yCoord))
        show_text(str(playerChar2.hpCurrent), (0, 0, 255), playerChar2.xCoord + 50, playerChar2.yCoord - 20)
    if playerChar3.alive == True:
        screen.blit(playerChar3.image, (playerChar3.xCoord,playerChar3.yCoord))
        show_text(str(playerChar3.hpCurrent), (0, 0, 255), playerChar3.xCoord + 50, playerChar3.yCoord - 20)

    if AIFighter.alive == True:
        screen.blit(FIGHTERimageAI, (AIFighter.xCoord,AIFighter.yCoord))
        show_text(str(AIFighter.hpCurrent), (255, 0, 0), AIFighter.xCoord + 50, AIFighter.yCoord - 20)

    if AITank.alive == True:
        screen.blit(TANKimageAI, (AITank.xCoord,AITank.yCoord))
        show_text(str(AITank.hpCurrent), (255, 0, 0), AITank.xCoord + 50, AITank.yCoord - 20)
    if AIFighter2.alive == True:
        screen.blit(FIGHTERimageAI, (AIFighter2.xCoord,AIFighter2.yCoord))
        show_text(str(AIFighter2.hpCurrent), (255, 0, 0), AIFighter2.xCoord + 50, AIFighter2.yCoord - 20)
    pygame.display.flip()


def move(attacker, defender):
    originalX = attacker.xCoord
    originalY = attacker.yCoord

    for _ in range(30):
        attacker.xCoord = attacker.xCoord + (defender.xCoord - originalX)/30
        attacker.yCoord = attacker.yCoord + (defender.yCoord - originalY)/30
        refreshScreen()
        pygame.display.flip() 
        time.sleep(0.01)

    attacker.xCoord = originalX
    attacker.yCoord = originalY
    refreshScreen()

def CheckAliveAll():
    playerChar1.checkAlive()
    playerChar2.checkAlive()
    playerChar3.checkAlive()
    AIFighter.checkAlive()
    AITank.checkAlive()
    AIFighter2.checkAlive()






playerChar1 = ChooseChar(0, 150)
playerChar2 = ChooseChar(100, 300)
playerChar3 = ChooseChar(0, 450)
AIFighter = pygameClasses.character(850, 150, 150, 50, 10, FIGHTERimageAI, True , 0)
AITank = pygameClasses.character(750, 300, 200, 30, 20, TANKimageAI, True , 0)
AIFighter2 = pygameClasses.character(870, 450, 120, 20, 10, FIGHTERimageAI, True , 0)



# print BG and characters

refreshScreen()


            
gamestate = 1
# gamestate 0 = waiting, gamsestate 1 = players attack, gamestate 2 = ai attack

(mouseX, mouseY) = pygame.mouse.get_pos()

pygame.display.flip()
clock = pygame.time.Clock()
running = True 
turn = 0  
playerList = [playerChar1, playerChar2, playerChar3]   
AIlist = [AIFighter, AITank, AIFighter2] 
def CurrAttacker(index):
    global turn
    if turn % 2 == 1:
        return AIlist[index - 1]
    elif turn % 2 == 0:
        return playerList[index - 1]

def CurrDefender(index):
    global turn
    if turn % 2 == 1:
        return playerList[index - 1]
    elif turn % 2 == 0:
        return AIlist[index - 1]

  

def playerTurn():
    global turn, gamestate
    SelectA = None
    SelectD = None
    PlayerHasAttacked = False   
    

    while PlayerHasAttacked == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                print("SA",SelectA)

#get number from keydown and use it to choose attacker
                if SelectA == None:
                
                    key = (chr(int(event.key)))  
                    print("A1",key)
                    if key not in ['1', '2', '3']:
                        pass
                    else:
                        Attacker = CurrAttacker(int(key))
                        if Attacker.alive == True:
                            SelectA = True
                        elif Attacker.alive == False:
                            pass
                elif SelectA == True and SelectD == None:
                    key = (chr(int(event.key)))
                    print("D1",key)
                    if key not in ['1', '2', '3']:
                        pass
                    else:
                        Defender = CurrDefender(int(key))
                        if Defender.alive == True:
                            SelectD = True
                        else:
                            pass
                        
                if SelectA == True and SelectD == True:
                    if Attacker.alive == True and Defender.alive == True:
                        move(Attacker, Defender)
                        Defender.takeDMG(Attacker.attack)
                        PlayerHasAttacked = True
                        SelectA = None
                        SelectD = None
                        Defender = None
                        Attacker = None
                else:
                        pass     



def winCondition():
    if AIFighter.alive == False and AIFighter2.alive == False and AITank.alive == False:
       print("Win")
       return True
    else:
        pass

       # pygame.quit()



def AIturn():
    global turn, gamestate
    Attacker = CurrAttacker(random.randint(0,2)) 
    Defender = CurrDefender(random.randint(0,2)) 
    while Attacker.alive == False or Attacker == None:
        Rand = random.randint(0,2)
        Attacker = CurrAttacker(Rand)
        print("Random Attacker", Rand)
    
    while Defender.alive == False or Defender == None:
        Rand = random.randint(0,2)
        Defender = CurrDefender(Rand)
        print("Random Defender", Rand)

    if Attacker.alive == True and Defender.alive == True:
        move(Attacker, Defender)
        Defender.takeDMG(Attacker.attack)
    # elif AIFighter.alive == False and AIFighter2.alive == False and AITank.alive == False:
    #    print("Win")
    #    # pygame.quit()
    else:
        pass
    
# main loop to keep window open (pygame.QUIT is the event type when the cross is pressed)
while running == True:
    clock.tick(60)
    

    if gamestate == 0:
        refreshScreen()
        
        
    elif gamestate == 1:
        refreshScreen()
        winCondition()
        playerTurn()

        turn += 1
        gamestate = 2
    elif gamestate == 2:
        refreshScreen()
        winCondition()
        if winCondition() == True:
            pass
        else:
            AIturn()

        turn += 1
        gamestate = 1



    for event in pygame.event.get():
    
        if event.type == pygame.QUIT:
            running = False
        
   

                






# required to uninitialise unnecessary resources if running game as a part of a larger program 
pygame.quit()

