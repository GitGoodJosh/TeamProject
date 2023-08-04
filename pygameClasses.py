import pygame


# define all classes here
class character(pygame.sprite.Sprite):
    def __init__(self, x, y, maxHp, Attack, Defense):
        self.xCoord = x
        self.yCoord = y 
        self.hpMax = maxHp
        self.hpCurrent = maxHp
        self.attack = Attack
        self.defense = Defense
    def move(self):
        self.position = (self.xCoord + 10, self.yCoord + 10)
    def applyDMG(self):
        return self.attack
    def takeDMG(self, attackApplied):
        self.hpCurrent = self.hpCurrent - (attackApplied - self.defense)
        return self.hpCurrent
    def healHP(self):
        self.hpCurrent = self.hpCurrent + (1/4)*(self.hpMax - self.hpCurrent)  
        

# tank and assassin are child classes of character so we dont have to keep defining functions (appliedDMG/takeDMG)
class tank(character):
    def __init__(self, x, y, maxHp, attack, defense):
        super().__init__(x, y, maxHp, attack, defense)


class fighter(character):
    def __init__(self, x, y, maxHp, attack, defense):
        super().__init__(x, y, maxHp, attack, defense)


class cleric(character):
    def __init__(self, x, y, maxHp, attack, defense):
        super().__init__(x, y, maxHp, attack, defense)





''' use test in pygame file dont run here
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
'''