
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


        







# define all classes here
class character():
    def __init__(self, x, y, maxHp, Attack, Defense, charImage, status: bool, exp):
        self.xCoord = x
        self.yCoord = y 
        self.hpMax = maxHp
        self.hpCurrent = maxHp
        self.attack = Attack
        self.defense = Defense
        self.image = charImage
        self.alive = status
        self.exp = exp
    def takeDMG(self, attackApplied):
        print(self.hpCurrent)
        self.hpCurrent = self.hpCurrent - (attackApplied - self.defense)
        print(self.hpCurrent)
    def checkAlive(self):
        #print(self.alive, self.image)
        if self.hpCurrent <= 0:
            self.alive = False
            self.image = None
            print(self.alive, self.image)

        else:
            pass
        
    

    
        

# tank and assassin are child classes of character so we dont have to keep defining functions (appliedDMG/takeDMG)
class fighter(character):
    def __init__(self, x, y, maxHp, attack, defense):
        super().__init__(x, y, maxHp, attack, defense)

class tank(character):
    def __init__(self, x, y, maxHp, attack, defense):
        super().__init__(x, y, maxHp, attack, defense)








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


'''


