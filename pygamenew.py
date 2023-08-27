import os
import time
import pygame
import pygameClasses
import random
import BGM

pygame.init()
# need list for pygame height and width (cannot usse two separate numbers)
screensize = (1000, 600)
# if changing bg pic remember to change size to fit 
#TeamGame\TeamProject\Assets\pygameBACKGROUND.png
pygame.display.set_mode(screensize)
pygame.display.set_caption(" GAME ")
pygame.mixer.pre_init(44100, 16, 2, 2048)

# Image Load Function
def LoadImg(img):
    try:
        return pygame.image.load(os.path.join(Asset_dir,img)).convert_alpha()
    except pygame.error:
        pass
def LoadImg2(Class_Dir,img):
    try:
        return pygame.image.load(os.path.join(Class_Dir,img)).convert_alpha()
    except pygame.error:
        pass

def FlipImg(img, horizontalFlip:bool, verticalFlip:bool):
    try:
        return pygame.transform.flip(img, horizontalFlip, verticalFlip)
    except TypeError:
        pass

def PlayBGM(bgm):
    try:
        pygame.mixer.music.load(os.path.join(Asset_dir,bgm))
        pygame.mixer.music.play(-1, 0.0)
    except pygame.error:
        pass

def PlaySFX(sfx):
    try:
        sfx2 =pygame.mixer.Sound(os.path.join(Asset_dir,sfx))
        sfx2.play()
    except pygame.error:
        pass

# load all images after this line
Asset_dir = os.path.join(os.path.dirname(__file__), 'Assets')
Warrior_dir = os.path.join(os.path.dirname(__file__), 'Assets', 'Warrior')
Warriorstand_dir = os.path.join(os.path.dirname(__file__), 'Assets', 'Warrior', 'Stand')
WarriorRun_dir = os.path.join(os.path.dirname(__file__), 'Assets', 'Warrior', 'Run')
WarriorAttack_dir = os.path.join(os.path.dirname(__file__), 'Assets', 'Warrior', 'Attack')

Tank_dir = os.path.join(os.path.dirname(__file__), 'Assets', 'Tank')
TankStand_dir = os.path.join(os.path.dirname(__file__), 'Assets', 'Tank', 'Stand')
TankRun_dir = os.path.join(os.path.dirname(__file__), 'Assets', 'Tank', 'Run')
TankAttack_dir = os.path.join(os.path.dirname(__file__), 'Assets', 'Tank', 'Attack')

StandList = [0,1,2,3,2]
RunList = [0,1,2,3,4]
AttackListW = [0,1,2,3,4]
AttackListT = [0,1,1,2,3]
G_index = 0
N_Counter = 0 #idleloop
H_index = 0
M_Counter = 0 #attackloop
SelectA = None
SelectD = None
PlayerHasAttacked = False
inAttack = None


BGimage = LoadImg('pygameBACKGROUND'+'.png')

StandTankImg   = FlipImg(LoadImg2(TankStand_dir,str(StandList[G_index])+'.png'),True,False)
StandWarriorImg   = FlipImg(LoadImg2(Warriorstand_dir,str(StandList[G_index])+'.png'),True,False)
AttackTankImg   = FlipImg(LoadImg2(TankStand_dir,str(AttackListT[G_index])+'.png'),True,False)
AttackWarriorImg   = FlipImg(LoadImg2(TankStand_dir,str(AttackListW[G_index])+'.png'),True,False)
InstructionImg = LoadImg('Picture1'+'.png')
InstructionImg2 = LoadImg('Picture2'+'.png')

TANKimage = StandTankImg
Warriorimage = StandWarriorImg

WarriorimageAI = FlipImg(Warriorimage, True, False)
TANKimageAI = FlipImg(TANKimage, True, False)
GlobalAttacker = None
GlobalDefender = None
GlobalX = None
GlobalY = None

screen = pygame.display.get_surface()

PlayBGM("Hene.wav")

# load all images before this line
# ------------------------------------------------- #
def Idleloop():
    global G_index, N_Counter, StandTankImg, StandWarriorImg, AttackTankImg, AttackWarriorImg
    N_Counter = N_Counter + 1
    if N_Counter >= 20:
        N_Counter = 0
        G_index = G_index + 1
        if G_index >= 5:
            G_index = 0

    StandTankImg   = FlipImg(LoadImg2(TankStand_dir,str(StandList[G_index])+'.png'),True,False)
    StandWarriorImg   = FlipImg(LoadImg2(Warriorstand_dir,str(StandList[G_index])+'.png'),True,False)

    
 #   print(StandTankImg)


def ChooseChar(x, y):
    CharChosen = False
    Char = None
    while CharChosen == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_t:
                    Char =  pygameClasses.character(x, y, 200, 50, 20, StandTankImg, True , 0)
                    Char.name = "tank"
                    Char.Class = 'Tank'
                    CharChosen = True
                    
                elif event.key == pygame.K_f:
                    Char = pygameClasses.character(x, y, 150, 70, 10, Warriorimage, True , 0)
                    Char.name = "Warrior"
                    Char.Class = 'Warrior'
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
    global inAttack
    Idleloop()
    for char in playerList:
        if char.Class == 'Tank' and char != inAttack:
            char.image = StandTankImg
        if char.Class == 'Warrior'and char != inAttack:
            char.image = StandWarriorImg
    for char in AIlist:
        if char.Class == 'Tank' and char != inAttack:
            char.image = FlipImg(StandTankImg, True, False)
        if char.Class == 'Warrior' and char != inAttack:
            char.image = FlipImg(StandWarriorImg, True, False)
    screen.blit(BGimage, (0,0))
    for char in playerList:
        if char.alive == True:
            screen.blit(char.image, (char.xCoord,char.yCoord))
            show_text(str(char.name).title(), (255, 255, 255), char.xCoord + 10, char.yCoord - 95, 25)
            show_text(str("Rank: ") + str(char.rank), (0, 0, 255), char.xCoord + 10, char.yCoord - 80, 25)
            show_text(str("HP: ") + str(char.hpCurrent), (0, 0, 255), char.xCoord + 10, char.yCoord - 65, 25)
            show_text(str("EXP: ") + str(char.exp), (0, 0, 255), char.xCoord + 10, char.yCoord - 50, 25)
            show_text(str("ATK: ") + str(char.attack), (0, 0, 255), char.xCoord + 10, char.yCoord - 35, 25)
            show_text(str("DEF: ") + str(char.defense), (0, 0, 255), char.xCoord + 10, char.yCoord - 20, 25)    
        else:
            pass
    for char in AIlist:
        if char.alive == True:
            screen.blit(char.image, (char.xCoord,char.yCoord))
            show_text(str(char.name).title(), (255, 255, 255), char.xCoord + 10, char.yCoord - 95,25)
            show_text(str("Rank: ") + str(char.rank), (255, 0, 0), char.xCoord + 10, char.yCoord - 80, 25)
            show_text(str("HP: ") + str(char.hpCurrent), (255, 0, 0), char.xCoord + 10, char.yCoord - 65, 25)
            show_text(str("EXP: ") + str(char.exp), (255, 0, 0), char.xCoord + 10, char.yCoord - 50, 25)
            show_text(str("ATK: ") + str(char.attack), (255, 0, 0), char.xCoord + 10, char.yCoord - 35, 25)
            show_text(str("DEF: ") + str(char.defense), (255, 0, 0), char.xCoord + 10, char.yCoord - 20, 25)
        else:
            pass

    pygame.display.flip()
AttackLoopCounter = 0

def AttackLoop(loop_number):
    global H_index, M_Counter, AttackTankImg, AttackWarriorImg, AttackLoopCounter
    #print(str(H_index))
    M_Counter = M_Counter + 1
    AttackLoopCounter += 1
    if loop_number > 40:
        return "done"
    if M_Counter >= 10:
        M_Counter = 0
        H_index = H_index + 1
        if H_index >= 5:
            H_index = 0
            

    AttackTankImg   = FlipImg(LoadImg2(TankAttack_dir,str(AttackListT[H_index])+'.png'),True,False)
    AttackWarriorImg   = FlipImg(LoadImg2(WarriorAttack_dir,str(AttackListW[H_index])+'.png'),True,False)


def move(attacker, defender):
    global gamestate, GlobalAttacker, GlobalDefender , GlobalX, GlobalY, PlayerHasAttacked, AttackLoopCounter, inAttack

    TimeMove = 0.5 #time taken to move in seconds
    if gamestate != 3:
        GlobalX = attacker.xCoord
        GlobalY = attacker.yCoord
        GlobalAttacker = attacker
        GlobalDefender = defender
        gamestate = 3
    elif gamestate == 3:
        if 100 <= defender.xCoord - attacker.xCoord or defender.xCoord - attacker.xCoord <= -100: #and (defender.yCoord +100  >= attacker.yCoord >= defender.yCoord -100) == False:
            attacker.xCoord = attacker.xCoord + (defender.xCoord - GlobalX)/(60*TimeMove)
            attacker.yCoord = attacker.yCoord + (defender.yCoord -  GlobalY)/(60*TimeMove)
        

        if (100 >= defender.xCoord - attacker.xCoord >= -100): #or defender.xCoord - attacker.xCoord >= -100): #and (defender.yCoord +120  >= attacker.yCoord >= defender.yCoord -120):
            AttackLoop(AttackLoopCounter)

            inAttack = attacker
            if attacker.Class == 'Tank':
                if attacker in playerList:
                    attacker.image = AttackTankImg
                elif attacker in AIlist:
                    attacker.image = FlipImg(AttackTankImg, True, False)
            if attacker.Class == 'Warrior':
                if attacker in playerList:
                    attacker.image = AttackWarriorImg
                elif attacker in AIlist:
                    attacker.image = FlipImg(AttackWarriorImg, True, False)
            if AttackLoop(AttackLoopCounter) == "done":
                dmg = GlobalDefender.takeDMG(GlobalAttacker.attack)
                GlobalAttacker.exp += dmg
                game_log.append(f"{GlobalAttacker.name} attacked {GlobalDefender.name} for {dmg} damage\n") 
                AttackLoopCounter = 0
                if OriGamestate == 1:
                    gamestate = 2
                    attacker.xCoord = GlobalX
                    attacker.yCoord = GlobalY
                    GlobalAttacker = None
                    GlobalDefender = None 
                    PlayerHasAttacked = True
                    inAttack = None
                    PlaySFX("attack.wav")

                elif OriGamestate == 2:
                    gamestate = 1
                    attacker.xCoord = GlobalX
                    attacker.yCoord = GlobalY
                    GlobalAttacker = None
                    GlobalDefender = None 
                    inAttack = None
                    PlaySFX("attack.wav")

            else:
                return
            


        else:
            pass

InstPg = 1
while InstPg != 4:

    screen.fill((0, 0, 0))
    if InstPg == 1:
        screen.blit(InstructionImg, (0,0))
    elif InstPg == 2:
        screen.blit(InstructionImg2, (0,0))
    elif InstPg == 3:
        screen.blit(BGimage, (0,0))
        show_text("Choose Your Character. By Press Enter then (T/F)", (0, 0, 0), 100, 100, 50)
    elif InstPg == 4:
        break


    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_RETURN:
                InstPg += 1  
            else:
                pass



    

            


playerChar1 = ChooseChar(0, 180)
playerChar2 = ChooseChar(100, 330)
playerChar3 = ChooseChar(0, 480)
PlaySFX("transion.wav")

AIWarrior = pygameClasses.character(850, 180, 150, 70, 10, WarriorimageAI, True , 'Warrior')
AITank = pygameClasses.character(750, 330, 200, 50, 20, TANKimageAI, True , 'Tank')
AIWarrior2 = pygameClasses.character(870, 480, 150, 70, 10, WarriorimageAI, True , 'Warrior')

characters = {
            "playerChar1" : {"instance" : playerChar1 ,"rank" : 1, "death added?" : "no"},
            "playerChar2" : {"instance" : playerChar2 ,"rank" :1, "death added?" : "no"},
            "playerChar3" : {"instance" : playerChar3 ,"rank" :1, "death added?" : "no"},
            "AIWarrior" : {"instance" : AIWarrior ,"rank" :1, "death added?" : "no"},
            "AITank" : {"instance" : AITank ,"rank" :1, "death added?" : "no"},
            "AIWarrior2" : {"instance" : AIWarrior2 ,"rank" :1, "death added?" : "no"},
}


# a=b=c=d=e=f=g=h=i=j=k=l=0
 #need these to make sure the function doesnt keep adding death logs every time its called
def CheckAliveAll():
    global characters
    for i in characters.keys():
        j = characters[i]
        char = j["instance"]
        if char.checkAliveEXP()[0] == False and j["death added?"] == "no":
            game_log.append(f"{char.name} died\n")
            j["death added?"] = "yes"
        if isinstance(char.checkAliveEXP()[1], int) and j["rank"] != char.rank and char.alive == True:
            game_log.append(f"{char.name} was promoted to rank {char.rank}\n")
            j["rank"] = int(char.rank)
            print("Level up! Alive")
            PlaySFX("levelup.wav")
            
        


game_log = ["game started\n"]

playerList = [playerChar1, playerChar2, playerChar3]   
AIlist = [AIWarrior, AITank, AIWarrior2] 
i = 0
for char in playerList:  
    i += 1
    nameChosen = False
    charNameByPlayer = ""
    screen.fill((0, 0, 0))
    modA = False
    while nameChosen == False: 
        show_text( "what would you like to name " + str(char.name) + f" (character number {i})", (255, 255, 255), 120, 100, 40)
        show_text(str(charNameByPlayer), (255, 255, 255), 250, 300, 70)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                    modA = True
                    continue
                if modA == True and event.key in range(97, 123):
                    letter = chr(int(event.key)-32)
                    modA = False
                elif modA == False:
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
                
PlaySFX("transion.wav")
# print BG and characters

refreshScreen()


            
gamestate = 1
# gamestate 0 = waiting, gamsestate 1 = players attack, gamestate 2 = ai attack gamestate 3 = moving


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

Defender = None
Attacker  = None

def playerTurn(key):
#    SelectA = None
#    SelectD = None
    global SelectA, SelectD, Defender, Attacker, PlayerHasAttacked, turn
    PlayerHasAttacked = False   
    

    if PlayerHasAttacked == False:
 #     
#get number from keydown and use it to choose attacker
                if SelectA == None:
                
                    try:# print("A1",key)
                        if key not in ['1', '2', '3']:
                            key = None
                        else:
                            Attacker = CurrAttacker(int(key))
                            key = None
                            if Attacker.alive == True:
                                SelectA = True
                            elif Attacker.alive == False:
                                Attacker = None

                                pass
                    except NameError:
                        pass
                elif SelectA == True and SelectD == None:  # choose defender using number keys
                    # print("D1",key)
                    try:
                        if key not in ['1', '2', '3']:
                            key = None
                        else:
                            Defender = CurrDefender(int(key))
                            key = None
                            if Defender.alive == True:
                                SelectD = True
                            else:
                                pass
                    except NameError:
                        pass
                                
                if SelectA == True and SelectD == True:
 #                   if Attacker.alive == True and Defender.alive == True:
                        move(Attacker, Defender)
                        PlayerHasAttacked = True
                        SelectA = None
                        SelectD = None
                        Defender = None
                        Attacker = None
                        turn += 1
 #               else:
  #                      pass     




def winCondition():
    if AIWarrior.alive == False and AIWarrior2.alive == False and AITank.alive == False:
        show_text("YOU WIN!!!", (0, 0, 255), 300, 100, 100)
        pygame.display.flip()
        return 1
    elif playerChar1.alive == False and playerChar2.alive == False and playerChar3.alive == False :
        show_text("YOU LOSE...", (255, 0, 0), 300, 100, 100)
        PlaySFX("lose.wav")
        pygame.display.flip()
        return 2
    else:
        pass




def AIturn():
    #print("AI turn")
    global turn, gamestate, GlobalAttacker, GlobalDefender
    if gamestate == 2:
        Attacker = CurrAttacker(random.randint(0,2)) 
        Defender = CurrDefender(random.randint(0,2)) # choose random attacker and defender
        while Attacker.alive == False or Attacker == None: #keep generating until attacker chosen is alive
            Rand = random.randint(0,2)
            Attacker = CurrAttacker(Rand)
        #    print("Random Attacker", Rand)
        
        while Defender.alive == False or Defender == None: # line 330 but for defender
            Rand = random.randint(0,2)
            Defender = CurrDefender(Rand)
        #    print("Random Defender", Rand)

        if Attacker.alive == True and Defender.alive == True: #carry out attack
            GlobalAttacker = Attacker
            GlobalDefender = Defender
            move(Attacker, Defender)
#            dmg = Defender.takeDMG(Attacker.attack)
#            game_log.append(f"{Attacker.name} attacked {Defender.name} for {dmg} damage\n")

    else:
            pass
playerWin = 0 
aiWin = 0
# main loop to keep window open (pygame.QUIT is the event type when the cross is pressed)


#BGM (Attack)
PlayBGM("Zak.wav")


#END BGM

while running == True:
    if playerWin == 0 and aiWin == 0:
        refreshScreen()
    ky = None

    for event in pygame.event.get():
    
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            ky = (chr(int(event.key)))
    
    clock.tick(60)

    if gamestate == 0:
    #    refreshScreen()
       pass 





        
    elif gamestate == 1:
        OriGamestate = gamestate
        if winCondition() == 2:
            if aiWin == 0:
                game_log.append("AI won")
                aiWin += 1   
                print(*game_log) 
        else:
            try: 
                playerTurn(ky)
            except NameError: #avoid getting error when the while loop tries to get events in playerturn function after the screen has been closed
                pass
                #running = False #stop the while loop

        
    elif gamestate == 2:
        OriGamestate = gamestate
    #    refreshScreen()
        if winCondition() == 1:
            if playerWin == 0:
                game_log.append("player won")
                playerWin += 1
                print(*game_log)
                PlayBGM("win.wav")
        else:
            AIturn()

        turn += 1

    elif gamestate == 3:
    #    refreshScreen()
        move(GlobalAttacker, GlobalDefender)




        
   

                






# required to uninitialise unnecessary resources if running game as a part of a larger program 
pygame.quit()


