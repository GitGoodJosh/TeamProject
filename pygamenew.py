import os
import time
import pygame
import pygameClasses
import random

pygame.init()
# need list for pygame height and width (cannot usse two separate numbers)
screensize = (1000, 600)
# note: used 1824x932 because thats the size of the pic
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
FIGHTERimage = LoadImg('pygameFIGHTER.png') # 142 x 153
HEALERimage = LoadImg('pygameHEALER.png')
FIGHTERimageAI = FlipImg(FIGHTERimage,True,False)
TANKimageAI = FlipImg(TANKimage, True, False)
HEALERimageAI = FlipImg(HEALERimage, True, False)
startButton = LoadImg('startButton.png')
attackButton = LoadImg('attackButton.png')
healButton = LoadImg('healButton.png')
startButton = pygame.transform.scale(startButton, (110,90))


# load all images before this line
# ------------------------------------------------- #


playerFighter = pygameClasses.character(0, 150, 150, 50, 10, FIGHTERimage)
playerTank = pygameClasses.character(100, 300, 200, 30, 20, TANKimage)
playerCleric = pygameClasses.character(0, 450, 120, 20, 10, HEALERimage)
AIFighter = pygameClasses.character(850, 150, 150, 50, 10, FIGHTERimageAI)
AITank = pygameClasses.character(750, 300, 200, 30, 20, TANKimageAI)
AICleric = pygameClasses.character(870, 450, 120, 20, 10, HEALERimageAI)



# print BG and characters
screen = pygame.display.get_surface()
screen.blit(BGimage, (0,0))
screen.blit(FIGHTERimage, (0,150))
screen.blit(TANKimage, (100,300))
screen.blit(HEALERimage, (0,450))
screen.blit(FIGHTERimageAI, (850,150))
screen.blit(TANKimageAI, (750,300))
screen.blit(HEALERimageAI, (870,450))
pygame.display.flip()

def blitAllexcept(exception):
    if exception == None:
        screen.blit(BGimage, (0,0))
        screen.blit(FIGHTERimage, (0,150))
        screen.blit(TANKimage, (100,300))
        screen.blit(HEALERimage, (0,450))
        screen.blit(FIGHTERimageAI, (850,150))
        screen.blit(TANKimageAI, (750,300))
        screen.blit(HEALERimageAI, (870,450))
    elif exception == FIGHTERimage:   
        screen.blit(BGimage, (0,0))
        screen.blit(TANKimage, (100,300))
        screen.blit(HEALERimage, (0,450))
        screen.blit(FIGHTERimageAI, (850,150))
        screen.blit(TANKimageAI, (750,300))
        screen.blit(HEALERimageAI, (870,450))
        
    elif exception == TANKimage:
        screen.blit(BGimage, (0,0))
        screen.blit(FIGHTERimage, (0,150))
        screen.blit(HEALERimage, (0,450))
        screen.blit(FIGHTERimageAI, (850,150))
        screen.blit(TANKimageAI, (750,300))
        screen.blit(HEALERimageAI, (870,450))

    elif exception == HEALERimage:
        screen.blit(BGimage, (0,0))
        screen.blit(FIGHTERimage, (0,150))
        screen.blit(TANKimage, (100,300))
        screen.blit(FIGHTERimageAI, (850,150))
        screen.blit(TANKimageAI, (750,300))
        screen.blit(HEALERimageAI, (870,450))

    elif exception == FIGHTERimageAI:
        screen.blit(BGimage, (0,0))
        screen.blit(FIGHTERimage, (0,150))
        screen.blit(TANKimage, (100,300))
        screen.blit(HEALERimage, (0,450))
        screen.blit(TANKimageAI, (750,300))
        screen.blit(HEALERimageAI, (870,450))


    elif exception == TANKimageAI:
        screen.blit(BGimage, (0,0))
        screen.blit(FIGHTERimage, (0,150))
        screen.blit(TANKimage, (100,300))
        screen.blit(HEALERimage, (0,450))
        screen.blit(FIGHTERimageAI, (850,150))
        screen.blit(HEALERimageAI, (870,450))

    elif exception == HEALERimageAI:
        screen.blit(BGimage, (0,0))
        screen.blit(FIGHTERimage, (0,150))
        screen.blit(TANKimage, (100,300))
        screen.blit(HEALERimage, (0,450))
        screen.blit(FIGHTERimageAI, (850,150))
        screen.blit(TANKimageAI, (750,300))

def move(attacker, defender):
    CHARACTERx = attacker.xCoord
    CHARACTERy = attacker.yCoord
    originalX = attacker.xCoord
    originalY = attacker.yCoord
    targetX = defender.xCoord
    targetY = defender.yCoord

    for i in range(30):
        blitAllexcept(attacker.image)
        pygame.display.flip()
        CHARACTERx = CHARACTERx + (targetX - originalX)/30
        CHARACTERy = CHARACTERy + (targetY - originalY)/30
        screen.blit(attacker.image, (CHARACTERx, CHARACTERy))
        pygame.display.flip()
        time.sleep(0.01)


    blitAllexcept(None)
    pygame.display.flip()

        







            
gamestate = 1
# gamestate 0 = waiting, gamsestate 1 = players attack, gamestate 2 = ai attack

(mouseX, mouseY) = pygame.mouse.get_pos()

pygame.display.flip()
clock = pygame.time.Clock()
running = True 
turn = 0  
playerList = [playerFighter, playerTank, playerCleric]   
AIlist = [AIFighter, AITank, AICleric] 
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
        blitAllexcept(None)
        pygame.display.flip()
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

