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
                    Char =  pygameClasses.character(x, y, 200, 50, 20, TANKimage, True , 0)
                    Char.name = "tank"
                    CharChosen = True
                    
                elif event.key == pygame.K_f:
                    Char = pygameClasses.character(x, y, 150, 70, 10, FIGHTERimage, True , 0)
                    Char.name = "fighter"

                    CharChosen = True
    return Char

pygame.font.SysFont.__init__()
def show_text( msg, color, x, y, size = 30 ):
    try:
        font = pygame.font.SysFont(None, size)
        text = font.render( msg, True, color)
        screen.blit(text, ( x, y ) )
    except:
        pygame.error

def refreshScreen():
    CheckAliveAll()

    screen.blit(BGimage, (0,0))
    if playerChar1.alive == True:
        screen.blit(playerChar1.image, (playerChar1.xCoord,playerChar1.yCoord))
        show_text(str("HP: ") + str(playerChar1.hpCurrent), (0, 0, 255), playerChar1.xCoord + 50, playerChar1.yCoord - 20)
        show_text(str("EXP: ") + str(playerChar1.exp), (0, 0, 255), playerChar1.xCoord + 50, playerChar1.yCoord - 40)
        show_text(str(playerChar1.name).title(), (255, 255, 255), playerChar1.xCoord + 50, playerChar1.yCoord - 60)




    if playerChar2.alive == True:
        screen.blit(playerChar2.image, (playerChar2.xCoord,playerChar2.yCoord))
        show_text(str("HP: ") + str(playerChar2.hpCurrent), (0, 0, 255), playerChar2.xCoord + 50, playerChar2.yCoord - 20)
        show_text(str("EXP: ") + str(playerChar2.exp), (0, 0, 255), playerChar2.xCoord + 50, playerChar2.yCoord - 40)
        show_text(str(playerChar2.name).title(), (255, 255, 255), playerChar2.xCoord + 50, playerChar2.yCoord - 60)


    if playerChar3.alive == True:
        screen.blit(playerChar3.image, (playerChar3.xCoord,playerChar3.yCoord))
        show_text(str("HP: ") + str(playerChar3.hpCurrent), (0, 0, 255), playerChar3.xCoord + 50, playerChar3.yCoord - 20)
        show_text(str("EXP: ") + str(playerChar3.exp), (0, 0, 255), playerChar3.xCoord + 50, playerChar3.yCoord - 40)
        show_text(str(playerChar3.name).title(), (255, 255, 255), playerChar3.xCoord + 50, playerChar3.yCoord - 60)



    if AIFighter.alive == True:
        screen.blit(FIGHTERimageAI, (AIFighter.xCoord,AIFighter.yCoord))
        show_text(str("HP: ") + str(AIFighter.hpCurrent), (255, 0, 0), AIFighter.xCoord + 50, AIFighter.yCoord - 20)
        show_text(str("EXP: ") + str(AIFighter.exp), (255, 0, 0), AIFighter.xCoord + 50, AIFighter.yCoord - 40)
        show_text(str(AIFighter.name).title(), (255, 255, 255), AIFighter.xCoord + 50, AIFighter.yCoord - 60)


    if AITank.alive == True:
        screen.blit(TANKimageAI, (AITank.xCoord,AITank.yCoord))
        show_text(str("HP: ") + str(AITank.hpCurrent), (255, 0, 0), AITank.xCoord + 50, AITank.yCoord - 20)
        show_text(str("EXP: ") + str(AITank.exp), (255, 0, 0), AITank.xCoord + 50, AITank.yCoord - 40)
        show_text(str(AITank.name).title(), (255, 255, 255), AITank.xCoord + 50, AITank.yCoord - 60)

    if AIFighter2.alive == True:
        screen.blit(FIGHTERimageAI, (AIFighter2.xCoord,AIFighter2.yCoord))
        show_text(str("HP: ") + str(AIFighter2.hpCurrent), (255, 0, 0), AIFighter2.xCoord + 50, AIFighter2.yCoord - 20)
        show_text(str("EXP: ") + str(AIFighter2.exp), (255, 0, 0), AIFighter2.xCoord + 50, AIFighter2.yCoord - 40)
        show_text(str(AIFighter2.name).title(), (255, 255, 255), AIFighter2.xCoord + 50, AIFighter2.yCoord - 60)

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
    playerChar1.checkAliveEXP()
    playerChar2.checkAliveEXP()
    playerChar3.checkAliveEXP()
    AIFighter.checkAliveEXP()
    AITank.checkAliveEXP()
    AIFighter2.checkAliveEXP()



            


playerChar1 = ChooseChar(0, 150)
playerChar2 = ChooseChar(100, 300)
playerChar3 = ChooseChar(0, 450)
AIFighter = pygameClasses.character(850, 150, 150, 70, 10, FIGHTERimageAI, True , 0)
AITank = pygameClasses.character(750, 300, 200, 50, 20, TANKimageAI, True , 0)
AIFighter2 = pygameClasses.character(870, 450, 150, 70, 10, FIGHTERimageAI, True , 0)

playerList = [playerChar1, playerChar2, playerChar3]   
AIlist = [AIFighter, AITank, AIFighter2] 
i = 0
for char in playerList:  
    i += 1
    nameChosen = False
    charNameByPlayer = ""
    screen.fill((0, 0, 0))
    while nameChosen == False: 
        show_text( "what would you like to name " + str(char.name) + f" (character number {i})", (255, 255, 255), 120, 100, 40)
        show_text(str(charNameByPlayer), (255, 255, 255), 250, 500)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                letter = chr(int(event.key))
                if event.key == pygame.K_RETURN:
                    char.name = charNameByPlayer
                    nameChosen = True
                else:
                    charNameByPlayer = charNameByPlayer + letter
                

# print BG and characters

refreshScreen()


            
gamestate = 1
# gamestate 0 = waiting, gamsestate 1 = players attack, gamestate 2 = ai attack

(mouseX, mouseY) = pygame.mouse.get_pos()

pygame.display.flip()
clock = pygame.time.Clock()
running = True 
turn = 0  

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
    clock.tick(100)
    

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

