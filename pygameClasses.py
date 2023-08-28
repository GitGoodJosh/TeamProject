import random
# need to load all this here to make the functions work here so the other page looks cleaner
import time

# define all classes here
class character():
    def __init__(self, x, y, maxHp, Attack, Defense, charImage, status: bool, Class):
        self.xCoord = x
        self.yCoord = y 
        self.hpMax = maxHp
        self.hpCurrent = maxHp
        self.attack = Attack
        self.defense = Defense
        self.image = charImage
        self.alive = status
        self.exp = 0
        self.name = str("AI" + str(random.randint(0,99)))
        self.rank = 1
        self.Class = Class
    def takeDMG(self, attackApplied):
        #print(self.hpCurrent)
        damage = attackApplied - self.defense + random.randint(-10, 10)
        self.hpCurrent = self.hpCurrent - damage
        if damage < 55:    
            self.exp += 5 * self.defense
        elif damage >= 55:
            self.exp += 2 * self.defense
        return damage        
    def checkAliveEXP(self):
        if self.hpCurrent <= 0:
            self.alive = False
            self.image = None

            
        if self.exp >= 100:
            #from pygamenew import PlaySFX
            self.hpCurrent += 30
            self.attack += 20
            self.exp -= 100
            self.rank += 1
            #print("Level up! C")
        
        return [self.alive, self.rank]


            


            
        
    

    
        

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


