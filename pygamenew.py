import os
import time
import pygame
import pygameClasses
from pygameClasses import tank
from pygameClasses import fighter
pygame.init()
# need list for pygame height and width (cannot usse two separate numbers)
screensize = (1000, 600)
# note: used 1824x932 because thats the size of the pic
# if changing bg pic remember to change size to fit 

pygame.display.set_mode(screensize)
pygame.display.set_caption(" GAME ")
# load all images after this line
BGimage = pygame.image.load(os.path.join('Assets','pygameBACKGROUND.png')).convert_alpha()
TANKimage = pygame.image.load(os.path.join('Assets','pygameTANK.png')).convert_alpha()
FIGHTERimage = pygame.image.load(os.path.join('Assets','pygameFIGHTER.png')).convert_alpha()
HEALERimage = pygame.image.load(os.path.join('Assets','pygameHEALER.png')).convert_alpha()
FIGHTERimageAI = pygame.transform.flip(FIGHTERimage, True, False)
TANKimageAI = pygame.transform.flip(TANKimage, True, False)
HEALERimageAI = pygame.transform.flip(HEALERimage, True, False)
# load all images before this line
# ------------------------------------------------- #
## T is first tank F is first fighter
# T = tank(400, 400, 200, 30, 20)
# F = fighter(600, 600, 150, 50, 10)


    


# print BG and characters
screen = pygame.display.get_surface()
screen.blit(BGimage, (0,0))
def setup(exception):
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
        

pygame.display.flip()


def moveFighter(CHARACTERx, CHARACTERy, targetX, targetY, CHARACTERimage = FIGHTERimage):


    originalX = CHARACTERx
    originalY = CHARACTERy

    for i in range(50):
        CHARACTERx = CHARACTERx + (targetX - originalX)/50
        CHARACTERy = CHARACTERy + (targetY - originalY)/50
        screen.blit(CHARACTERimage, (CHARACTERx, CHARACTERy))
        pygame.display.flip()
        time.sleep(0.05)
        setup(FIGHTERimage)

    screen.blit(CHARACTERimage, (originalX, originalY))
    pygame.display.flip()


            



            


    

clock = pygame.time.Clock()
running = True 
# main loop to keep window open (pygame.QUIT is the event type when the cross is pressed)
while running == True:
    moveFighter(0, 150, 700, 300)
    pygame.display.flip()
    




    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



# required to uninitialise unnecessary resources if running game as a part of a larger program 
pygame.quit()

