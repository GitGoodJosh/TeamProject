
import pygame
# need to load all this here to make the functions work here so the other page looks cleaner
import time
import os
pygame.init()
screensize = (1000, 600)
pygame.display.set_mode(screensize)
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
screen = pygame.display.get_surface()

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
        blitAllexcept(CHARACTERimage)
        pygame.display.flip()
        CHARACTERx = CHARACTERx + (targetX - originalX)/30
        CHARACTERy = CHARACTERy + (targetY - originalY)/30
        screen.blit(CHARACTERimage, (CHARACTERx, CHARACTERy))
        time.sleep(0.01)
        pygame.display.flip()

    screen.blit(CHARACTERimage, (originalX, originalY))
    pygame.display.flip()



# define all classes here
class character():
    def __init__(self, x, y, maxHp, Attack, Defense):
        self.xCoord = x
        self.yCoord = y 
        self.hpMax = maxHp
        self.hpCurrent = maxHp
        self.attack = Attack
        self.defense = Defense
    def applyDMG(self):
        return self.attack
    def takeDMG(self, attackApplied):
        self.hpCurrent = self.hpCurrent - (attackApplied - self.defense)
        return self.hpCurrent
    def healHP(self):
        self.hpCurrent = self.hpCurrent + (1/4)*(self.hpMax - self.hpCurrent) 
    def xCoordOf(self):
        return self.xCoord
    def yCoordOf(self):
        return self.yCoord
    
        

# tank and assassin are child classes of character so we dont have to keep defining functions (appliedDMG/takeDMG)
class fighter(character):
    def __init__(self, x, y, maxHp, attack, defense):
        super().__init__(x, y, maxHp, attack, defense)

class tank(character):
    def __init__(self, x, y, maxHp, attack, defense):
        super().__init__(x, y, maxHp, attack, defense)


class cleric(character):
    def __init__(self, x, y, maxHp, attack, defense):
        super().__init__( x, y, maxHp, attack, defense)





''' # testing fighter take dmg from tank hp = 150 - (30 - 10)
print(playerFighter.takeDMG(AITank.applyDMG()))
# yes
#testing if tank takes dmg properly output should be 200 - (50 - 20) = 170
print(AITank.takeDMG(playerFighter.applyDMG()))
#yes
# test if tank updates self.hp after taking hit (should show 170, 140, 110, 80...)
print(AITank.takeDMG(playerFighter.applyDMG()))
print(AITank.takeDMG(playerFighter.applyDMG()))
print(AITank.takeDMG(playerFighter.applyDMG()))

# yes
#test heal (1/4 of lost hp)
AITank.healHP()
print(AITank.hpCurrent)
# yes 
'''