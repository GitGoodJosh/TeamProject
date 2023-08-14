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
                    Char =  pygameClasses.character(x, y, 200, 30, 20, TANKimage)
                    CharChosen = True
                    
                elif event.key == pygame.K_f:
                    Char = pygameClasses.character(x, y, 150, 50, 10, FIGHTERimage)
                    CharChosen = True
    return Char

def refreshScreen():
    screen.blit(BGimage, (0,0))
    screen.blit(playerChar1.image, (playerChar1.xCoord,playerChar1.yCoord))
    screen.blit(playerChar2.image, (playerChar2.xCoord,playerChar2.yCoord))
    screen.blit(playerChar3.image, (playerChar3.xCoord,playerChar3.yCoord))
    screen.blit(FIGHTERimageAI, (AIFighter.xCoord,AIFighter.yCoord))
    screen.blit(TANKimageAI, (AITank.xCoord,AITank.yCoord))
    screen.blit(FIGHTERimageAI, (AIFighter2.xCoord,AIFighter2.yCoord))
    pygame.display.flip()

def move(attacker, defender):
    originalX = attacker.xCoord
    originalY = attacker.yCoord

    for i in range(30):
        attacker.xCoord = attacker.xCoord + (defender.xCoord - originalX)/30
        attacker.yCoord = attacker.yCoord + (defender.yCoord - originalY)/30
        refreshScreen()
        pygame.display.flip()
        time.sleep(0.01)

    attacker.xCoord = originalX
    attacker.yCoord = originalY
    refreshScreen()




playerChar1 = ChooseChar(0, 150)
playerChar2 = ChooseChar(100, 300)
playerChar3 = ChooseChar(0, 450)
AIFighter = pygameClasses.character(850, 150, 150, 50, 10, FIGHTERimageAI)
AITank = pygameClasses.character(750, 300, 200, 30, 20, TANKimageAI)
AIFighter2 = pygameClasses.character(870, 450, 120, 20, 10, FIGHTERimageAI)



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
    PlayerHasAttacked = False
    TargetHasBeenChosen = False
    while PlayerHasAttacked == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    Attacker = CurrAttacker(1)
                    while TargetHasBeenChosen == False:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                            elif event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_1:
                                    Defender = CurrDefender(1)
                                    move(Attacker, Defender)
                                    Defender.takeDMG(Attacker.attack)
                                    TargetHasBeenChosen = True
                                elif event.key == pygame.K_2:
                                    Defender = CurrDefender(2)
                                    move(Attacker, Defender)
                                    Defender.takeDMG(Attacker.attack)
                                    TargetHasBeenChosen = True
                                elif event.key == pygame.K_3:
                                    Defender = CurrDefender(3)
                                    move(Attacker, Defender)
                                    Defender.takeDMG(Attacker.attack)
                                    TargetHasBeenChosen = True
                                  
                    PlayerHasAttacked = True         
                elif event.key == pygame.K_2:
                    Attacker = CurrAttacker(2)
                    while TargetHasBeenChosen == False:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                            elif event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_1:
                                    Defender = CurrDefender(1)
                                    move(Attacker, Defender)
                                    Defender.takeDMG(Attacker.attack)
                                    TargetHasBeenChosen = True
                                elif event.key == pygame.K_2:
                                    Defender = CurrDefender(2)
                                    move(Attacker, Defender)
                                    Defender.takeDMG(Attacker.attack)
                                    TargetHasBeenChosen = True
                                elif event.key == pygame.K_3:
                                    Defender = CurrDefender(3)
                                    move(Attacker, Defender)
                                    Defender.takeDMG(Attacker.attack)
                                    TargetHasBeenChosen = True
                                
                    PlayerHasAttacked = True
                elif event.key == pygame.K_3:
                    Attacker = CurrAttacker(3)
                    while TargetHasBeenChosen == False:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                            elif event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_1:
                                    Defender = CurrDefender(1)
                                    move(Attacker, Defender)
                                    Defender.takeDMG(Attacker.attack)
                                    TargetHasBeenChosen = True
                                elif event.key == pygame.K_2:
                                    Defender = CurrDefender(2)
                                    move(Attacker, Defender)
                                    Defender.takeDMG(Attacker.attack)
                                    TargetHasBeenChosen = True
                                elif event.key == pygame.K_3:
                                    Defender = CurrDefender(3)
                                    move(Attacker, Defender)
                                    Defender.takeDMG(Attacker.attack)
                                    TargetHasBeenChosen = True            
                    PlayerHasAttacked = True


def AIturn():
    global turn, gamestate
    Attacker = CurrAttacker(random.randint(0,2))
    Defender = CurrDefender(random.randint(0,2))
    move(Attacker, Defender)
    Defender.takeDMG(Attacker.attack)

    
# main loop to keep window open (pygame.QUIT is the event type when the cross is pressed)
while running == True:

    if gamestate == 0:
        refreshScreen()
    elif gamestate == 1:
        playerTurn()
        turn += 1
        gamestate = 2
    elif gamestate == 2:
        AIturn()
        turn += 1
        gamestate = 1



    for event in pygame.event.get():
    
        if event.type == pygame.QUIT:
            running = False
        
   

                






# required to uninitialise unnecessary resources if running game as a part of a larger program 
pygame.quit()

