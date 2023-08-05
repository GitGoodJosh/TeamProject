import os
import time
import pygame
import sys 
from pygameClasses import cleric, tank, fighter, character

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
FIGHTERimage = LoadImg('pygameFIGHTER.png')
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

playerFighter = fighter(0, 150, 150, 50, 10)
playerTank = tank(100, 300, 200, 30, 20)
playerCleric = cleric(0, 450, 120, 20, 10)
AIFighter = fighter(850, 150, 150, 50, 10)
AITank = tank(750, 300, 200, 30, 20)
AICleric = cleric(870, 450, 120, 20, 10)



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
    if exception == FIGHTERimage:   
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
        



def move(CHARACTERimage, CHARACTERx, CHARACTERy, targetX, targetY):
    originalX = CHARACTERx
    originalY = CHARACTERy

    for i in range(30):
        CHARACTERx = CHARACTERx + (targetX - originalX)/30
        CHARACTERy = CHARACTERy + (targetY - originalY)/30
        screen.blit(CHARACTERimage, (CHARACTERx, CHARACTERy))
        pygame.display.flip()
        time.sleep(0.01)
        blitAllexcept(CHARACTERimage)

    screen.blit(CHARACTERimage, (originalX, originalY))
    pygame.display.flip()




            


(mouseX, mouseY) = pygame.mouse.get_pos()

pygame.display.flip()
clock = pygame.time.Clock()
running = True 
# main loop to keep window open (pygame.QUIT is the event type when the cross is pressed)
while running == True:
    clock.tick(60)
    screen.blit(startButton, (450, 300))
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and 450 < mouseX < 540 and 300 < mouseY < 390:
            move(FIGHTERimage, playerFighter.xCoordOf(), playerFighter.yCoordOf(), AITank.xCoordOf(), AITank.yCoordOf())
    pygame.display.flip()
    




    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



# required to uninitialise unnecessary resources if running game as a part of a larger program 
pygame.quit()

