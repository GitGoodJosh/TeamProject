import os
import time
import pygame
import sys 
import pygameClasses
import math
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
# gamestate 1 = waiting, gamsestate 0 = players attack, gamestate 2 = ai attack

(mouseX, mouseY) = pygame.mouse.get_pos()

pygame.display.flip()
clock = pygame.time.Clock()
running = True 
turn = 0  
playerList = [playerFighter, playerTank, playerCleric]   
AIlist = [AIFighter, AITank, AICleric] 
index = 0
def CurrAttacker():
    global index

    if index%2 == 0:
        attacker = playerList[int(index/2)]
    if index%2 == 1:
        attacker = AIlist[int(math.ceil(index/2)) - 1]
    if index > 6:
        index = 0
    print("ii",index)
    return attacker

    
# main loop to keep window open (pygame.QUIT is the event type when the cross is pressed)
while running == True:

    if gamestate == 1:
        blitAllexcept(None)
        pygame.display.flip()
    elif gamestate == 2:
        chosen = random.randint(0,2)
        move(CurrAttacker(), playerList[chosen])
        playerList[chosen].takeDMG(CurrAttacker().attack)
        gamestate = 1
        index += 1
        turn += 1


    for event in pygame.event.get():
    
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_1:
                gamestate = 0
                move(CurrAttacker(), AIlist[0])
                

                gamestate = 2
                AIlist[0].takeDMG(CurrAttacker().attack)
            
            if event.key == pygame.K_2:
                gamestate = 0
                move(CurrAttacker(), AIlist[1])  

                gamestate = 2
                AIlist[1].takeDMG(CurrAttacker().attack)

            if event.key == pygame.K_3:
                gamestate = 0
                move(CurrAttacker(), AIlist[2])      
                

                gamestate = 2
                AIlist[2].takeDMG(CurrAttacker().attack)
            turn += 1
            print(turn)





# required to uninitialise unnecessary resources if running game as a part of a larger program 
pygame.quit()

