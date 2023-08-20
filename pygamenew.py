import os
import time
import pygame
import pygameClasses
import random

pygame.init()
# need list for pygame height and width (cannot usse two separate numbers)
screensize = (1000, 600)
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
FIGHTERimageAI = FlipImg(FIGHTERimage, True, False)
TANKimageAI = FlipImg(TANKimage, True, False)


screen = pygame.display.get_surface()

# load all images before this line
# ------------------------------------------------- #
def ChooseChar(x, y):
    CharChosen = False
    Char = None
    while CharChosen == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_t:
                    Char =  pygameClasses.character(x, y, 200, 50, 20, TANKimage, True , 0)
                    Char.name = "tank"
                    CharChosen = True
                    
                elif event.key == pygame.K_f:
                    Char = pygameClasses.character(x, y, 150, 70, 10, FIGHTERimage, True , 0)
                    Char.name = "fighter"

                    CharChosen = True
    return Char

pygame.font.SysFont.__init__()
def show_text( msg, color, x, y, size = 30 ):
    try:
        font = pygame.font.SysFont(None, size)
        text = font.render( msg, True, color)
        screen.blit(text, ( x, y ) )
    except:
        pygame.error

def refreshScreen():
    CheckAliveAll()
    screen.blit(BGimage, (0,0))
    for char in (AIlist + playerList):
        if char.alive == True:
            screen.blit(char.image, (char.xCoord,char.yCoord))
            show_text(str("HP: ") + str(char.hpCurrent), (0, 0, 255), char.xCoord + 50, char.yCoord - 20)
            show_text(str("EXP: ") + str(char.exp), (0, 0, 255), char.xCoord + 50, char.yCoord - 40)
            show_text(str(char.name).title(), (255, 255, 255), char.xCoord + 50, char.yCoord - 60)
        else:
            pass




    '''if playerChar1.alive == True:
        screen.blit(playerChar1.image, (playerChar1.xCoord,playerChar1.yCoord))
        show_text(str("HP: ") + str(playerChar1.hpCurrent), (0, 0, 255), playerChar1.xCoord + 50, playerChar1.yCoord - 20)
        show_text(str("EXP: ") + str(playerChar1.exp), (0, 0, 255), playerChar1.xCoord + 50, playerChar1.yCoord - 40)
        show_text(str(playerChar1.name).title(), (255, 255, 255), playerChar1.xCoord + 50, playerChar1.yCoord - 60)

    if playerChar2.alive == True:
        screen.blit(playerChar2.image, (playerChar2.xCoord,playerChar2.yCoord))
        show_text(str("HP: ") + str(playerChar2.hpCurrent), (0, 0, 255), playerChar2.xCoord + 50, playerChar2.yCoord - 20)
        show_text(str("EXP: ") + str(playerChar2.exp), (0, 0, 255), playerChar2.xCoord + 50, playerChar2.yCoord - 40)
        show_text(str(playerChar2.name).title(), (255, 255, 255), playerChar2.xCoord + 50, playerChar2.yCoord - 60)

    if playerChar3.alive == True:
        screen.blit(playerChar3.image, (playerChar3.xCoord,playerChar3.yCoord))
        show_text(str("HP: ") + str(playerChar3.hpCurrent), (0, 0, 255), playerChar3.xCoord + 50, playerChar3.yCoord - 20)
        show_text(str("EXP: ") + str(playerChar3.exp), (0, 0, 255), playerChar3.xCoord + 50, playerChar3.yCoord - 40)
        show_text(str(playerChar3.name).title(), (255, 255, 255), playerChar3.xCoord + 50, playerChar3.yCoord - 60)

    if AIFighter.alive == True:
        screen.blit(FIGHTERimageAI, (AIFighter.xCoord,AIFighter.yCoord))
        show_text(str("HP: ") + str(AIFighter.hpCurrent), (255, 0, 0), AIFighter.xCoord + 50, AIFighter.yCoord - 20)
        show_text(str("EXP: ") + str(AIFighter.exp), (255, 0, 0), AIFighter.xCoord + 50, AIFighter.yCoord - 40)
        show_text(str(AIFighter.name).title(), (255, 255, 255), AIFighter.xCoord + 50, AIFighter.yCoord - 60)

    if AITank.alive == True:
        screen.blit(TANKimageAI, (AITank.xCoord,AITank.yCoord))
        show_text(str("HP: ") + str(AITank.hpCurrent), (255, 0, 0), AITank.xCoord + 50, AITank.yCoord - 20)
        show_text(str("EXP: ") + str(AITank.exp), (255, 0, 0), AITank.xCoord + 50, AITank.yCoord - 40)
        show_text(str(AITank.name).title(), (255, 255, 255), AITank.xCoord + 50, AITank.yCoord - 60)

    if AIFighter2.alive == True:
        screen.blit(FIGHTERimageAI, (AIFighter2.xCoord,AIFighter2.yCoord))
        show_text(str("HP: ") + str(AIFighter2.hpCurrent), (255, 0, 0), AIFighter2.xCoord + 50, AIFighter2.yCoord - 20)
        show_text(str("EXP: ") + str(AIFighter2.exp), (255, 0, 0), AIFighter2.xCoord + 50, AIFighter2.yCoord - 40)
        show_text(str(AIFighter2.name).title(), (255, 255, 255), AIFighter2.xCoord + 50, AIFighter2.yCoord - 60)'''

    pygame.display.flip()


def move(attacker, defender):
    originalX = attacker.xCoord
    originalY = attacker.yCoord

    for _ in range(30):
        attacker.xCoord = attacker.xCoord + (defender.xCoord - originalX)/30
        attacker.yCoord = attacker.yCoord + (defender.yCoord - originalY)/30
        refreshScreen()
        pygame.display.flip() 

    attacker.xCoord = originalX
    attacker.yCoord = originalY
    refreshScreen()






    

            


playerChar1 = ChooseChar(0, 150)
playerChar2 = ChooseChar(100, 300)
playerChar3 = ChooseChar(0, 450)
AIFighter = pygameClasses.character(850, 150, 15, 70, 10, FIGHTERimageAI, True , 0)
AITank = pygameClasses.character(750, 300, 20, 50, 20, TANKimageAI, True , 0)
AIFighter2 = pygameClasses.character(870, 450, 15, 70, 10, FIGHTERimageAI, True , 0)

characters = {
            "playerChar1" : {"instance" : playerChar1 ,"rank" : "1", "death added?" : "no"},
            "playerChar2" : {"instance" : playerChar2 ,"rank" :"1", "death added?" : "no"},
            "playerChar3" : {"instance" : playerChar3 ,"rank" :"1", "death added?" : "no"},
            "AIFighter" : {"instance" : AIFighter ,"rank" :"1", "death added?" : "no"},
            "AITank" : {"instance" : AITank ,"rank" :"1", "death added?" : "no"},
            "AIFighter2" : {"instance" : AIFighter2 ,"rank" :"1", "death added?" : "no"},
}


# a=b=c=d=e=f=g=h=i=j=k=l=0
 #need these to make sure the function doesnt keep adding death logs every time its called
def CheckAliveAll():
    global characters
    for i in characters.keys():
        j = characters[i]
        char = j["instance"]
        if char.checkAliveEXP() == False and j["death added?"] == "no":
            game_log.append(f"{char.name} died\n")
            j["death added?"] = "yes"
        elif isinstance(char.checkAliveEXP(), int) and j["rank"] != char.rank and char.alive == True:
            game_log.append(f"{char.name} was promoted to rank {char.rank}\n")
            j["rank"] = char.rank
        
    '''if playerChar1.checkAliveEXP() == False and a == 0:
        game_log.append(f"{playerChar1.name} died\n")
        a = 1
    elif isinstance(playerChar1.checkAliveEXP(), int) and :
        game_log.append(f"{playerChar1.name} was promoted to rank {playerChar1.rank}\n")

    if playerChar2.checkAliveEXP() == False and b == 0:
        game_log.append(f"{playerChar2.name} died\n")
        b = 1
    elif isinstance(playerChar2.checkAliveEXP(), int):
        game_log.append(f"{playerChar2.name} was promoted to rank {playerChar2.rank}\n")

    if playerChar3.checkAliveEXP() == False and c == 0:
        game_log.append(f"{playerChar3.name} died\n")
        c = 1
    elif isinstance(playerChar3.checkAliveEXP(), int):
        game_log.append(f"{playerChar3.name} was promoted to rank {playerChar3.rank}\n")

    if AIFighter.checkAliveEXP() == False and d == 0:
        game_log.append(f"{AIFighter.name} died\n")
        d = 1
    elif isinstance(AIFighter.checkAliveEXP(), int):
        game_log.append(f"{AIFighter.name} was promoted to rank {AIFighter.rank}\n")

    if AITank.checkAliveEXP() == False and e == 0:
        game_log.append(f"{AITank.name} died\n")
        e = 1
    elif isinstance(AITank.checkAliveEXP(), int):
        game_log.append(f"{AITank.name} was promoted to rank {AITank.rank}\n")

    if AIFighter2.checkAliveEXP() == False and f == 0:
        game_log.append(f"{AIFighter2.name} died\n")
        f = 1
    elif isinstance(AIFighter2.checkAliveEXP(), int):
        game_log.append(f"{AIFighter2.name} was promoted to rank {AIFighter2.rank}\n")
'''


game_log = ["game started\n"]

playerList = [playerChar1, playerChar2, playerChar3]   
AIlist = [AIFighter, AITank, AIFighter2] 
i = 0
for char in playerList:  
    i += 1
    nameChosen = False
    charNameByPlayer = ""
    screen.fill((0, 0, 0))
    while nameChosen == False: 
        show_text( "what would you like to name " + str(char.name) + f" (character number {i})", (255, 255, 255), 120, 100, 40)
        show_text(str(charNameByPlayer), (255, 255, 255), 250, 300, 70)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                letter = chr(int(event.key))
                if event.key == pygame.K_RETURN:
                    game_log.append(f"{char.name} was named {charNameByPlayer}\n")
                    char.name = charNameByPlayer
                    nameChosen = True
                elif event.key == pygame.K_BACKSPACE:
                    charNameByPlayer = charNameByPlayer[:len(charNameByPlayer) - 1]
                    screen.fill((0, 0, 0))
                    pygame.display.flip()
                else:
                    charNameByPlayer = charNameByPlayer + letter
                

# print BG and characters

refreshScreen()


            
gamestate = 1
# gamestate 0 = waiting, gamsestate 1 = players attack, gamestate 2 = ai attack


clock = pygame.time.Clock()
running = True 
turn = 0  

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
    SelectA = None
    SelectD = None
    PlayerHasAttacked = False   
    

    while PlayerHasAttacked == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                # print("SA",SelectA)

#get number from keydown and use it to choose attacker
                if SelectA == None:
                
                    key = (chr(int(event.key)))  
                    # print("A1",key)
                    if key not in ['1', '2', '3']:
                        pass
                    else:
                        Attacker = CurrAttacker(int(key))
                        if Attacker.alive == True:
                            SelectA = True
                        elif Attacker.alive == False:
                            pass
                elif SelectA == True and SelectD == None:  # choose defender using number keys
                    key = (chr(int(event.key)))
                    # print("D1",key)
                    if key not in ['1', '2', '3']:
                        pass
                    else:
                        Defender = CurrDefender(int(key))
                        if Defender.alive == True:
                            SelectD = True
                        else:
                            pass
                        
                if SelectA == True and SelectD == True:
                    if Attacker.alive == True and Defender.alive == True:
                        move(Attacker, Defender)
                        dmg = Defender.takeDMG(Attacker.attack)
                        game_log.append(f"{Attacker.name} attacked {Defender.name} for {dmg} damage\n")
                        PlayerHasAttacked = True
                        SelectA = None
                        SelectD = None
                        Defender = None
                        Attacker = None
                else:
                        pass     



def winCondition():
    if AIFighter.alive == False and AIFighter2.alive == False and AITank.alive == False:
       return True
    else:
        pass

       # pygame.quit()



def AIturn():
    global turn, gamestate
    Attacker = CurrAttacker(random.randint(0,2)) 
    Defender = CurrDefender(random.randint(0,2)) # choose random attacker and defender
    while Attacker.alive == False or Attacker == None: #keep generating until attacker chosen is alive
        Rand = random.randint(0,2)
        Attacker = CurrAttacker(Rand)
        print("Random Attacker", Rand)
    
    while Defender.alive == False or Defender == None: # line 330 but for defender
        Rand = random.randint(0,2)
        Defender = CurrDefender(Rand)
        print("Random Defender", Rand)

    if Attacker.alive == True and Defender.alive == True: #carry out attack
        move(Attacker, Defender)
        dmg = Defender.takeDMG(Attacker.attack)
        game_log.append(f"{Attacker.name} attacked {Defender.name} for {dmg} damage\n")

    else:
        pass
    
# main loop to keep window open (pygame.QUIT is the event type when the cross is pressed)
while running == True:
    for event in pygame.event.get():
    
        if event.type == pygame.QUIT:
            running = False
    
    
    clock.tick(60)

    if gamestate == 0:
        refreshScreen()
        
        
    elif gamestate == 1:
        refreshScreen()
        winCondition()
        try: 
            playerTurn()
        except pygame.error: #avoid getting error when the while loop tries to get events in playerturn function after the screen has been closed
            running = False #stop the while loop

        turn += 1
        gamestate = 2
    elif gamestate == 2:
        refreshScreen()
        if winCondition() == True:
            game_log.append("player won")
            gamestate = 1
        else:
            AIturn()

        turn += 1
        gamestate = 1


        
   

                






# required to uninitialise unnecessary resources if running game as a part of a larger program 
pygame.quit()

print(*game_log)
