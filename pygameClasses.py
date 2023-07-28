# define all classes here
class character:
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
        

# tank and assassin are child classes of character so we dont have to keep defining functions (appliedDMG/takeDMG)
class tank(character):
    def __init__(self, x, y, maxHp, attack, defense):
        super().__init__(x, y, maxHp, attack, defense)


class fighter(character):
    def __init__(self, x, y, maxHp, attack, defense):
        super().__init__(x, y, maxHp, attack, defense)






