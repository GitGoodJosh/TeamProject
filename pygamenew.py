import os
import pygame
from pygameClasses import tank
from pygameClasses import fighter
pygame.init()
# need list for pygame height and width (cannot usse two separate numbers)
screensize = (1824, 932)
# note: used 1824x932 because thats the size of the pic
# if changing bg pic remember to change size to fit 

pygame.display.set_mode(screensize)
pygame.display.set_caption(" GAME ")
# load all images after this line
BGimage = pygame.image.load(os.path.join('Assets','pygameBG.png')).convert_alpha()
TANKimage = pygame.image.load(os.path.join('Assets','pygameBG.png')).convert_alpha()
FIGHTERimage = pygame.image.load(os.path.join('Assets','pygameBG.png')).convert_alpha()
HEALERimage = pygame.image.load(os.path.join('Assets','pygameBG.png')).convert_alpha()
# load all images before this line
# ------------------------------------------------- #









# print BGimage
pygame.display.get_surface().blit(BGimage, (0,0))
pygame.display.get_surface().blit(TANKimage, (0,0))
pygame.display.get_surface().blit(FIGHTERimage, (0,150))
pygame.display.get_surface().blit(HEALERimage, (0,300))
# main loop to keep window open (pygame.QUIT is the event type when the cross is pressed)
running = True 
while running == True:
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


# required to uninitialise unnecessary resources if running game as a part of a larger program 
pygame.quit

# T is first tank F is first fighter
T = tank(400, 400, 200, 30, 20)
F = fighter(600, 600, 150, 50, 10)

# testing fighter take dmg from tank hp = 150 - (30 - 10)
print(F.takeDMG(T.applyDMG()))
# yes
#testing if tank takes dmg properly output should be 200 - (50 - 20) = 170
print(T.takeDMG(F.applyDMG()))
#yes
# test if tank updates self.hp after taking hit (should show 170, 140, 110, 80...)
print(T.takeDMG(F.applyDMG()))
print(T.takeDMG(F.applyDMG()))
print(T.takeDMG(F.applyDMG()))

# yes
#test heal (1/4 of lost hp)
T.healHP()
print(T.hpCurrent)
# yes