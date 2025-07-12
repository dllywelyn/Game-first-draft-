import time
import os
import random


BK   = '\033[30m'
R     = '\033[31m'
G   = '\033[32m'
Y  = '\033[33m'
B    = '\033[34m'
M = '\033[35m'
C    = '\033[36m'
W   = '\033[37m'

r = '\033[39m' # reset colour (keeps bold and other effects)
b = '\033[1m' #Bold
o = '\033[0m'#0ff
colours = {R:"RED", G:"GREEN", B:"BLUE", Y:"YELLOW", M:"MAGENTA", C:"CYAN"}
#print(" ".join(colours.values()))  # keys  i.e. words
name1 = input("What's your name?")
choice = int(input("\n   How do you fancy yourself? \
\n   A strong, powerful fighter? [1] \n   An agile and stealthy thief? [2]\
\n   Or a master of disguise? [3]"))
if (choice == 1):
    char = "fighter"
    charfont = f"\033[1m{R}"
    charfontw = f"{charfont}{[value for value in colours.values()][0]}\033[0m"  #designates colour word in colour
    colours.pop(R)  # deletes item from list whilst keeping the variable value (unlike from 'del')
    adj1 = "meatheaded savage"
    adj2 = "an aggressive brute"
    title = f"{charfont}{name1} the Violent{o}"
    
if (choice == 2):
    char = "thief"
    charfont = f"\033[1m{G}"
    charfontw = f"{charfont}{[value for value in colours.values()][1]}\033[0m"
    colours.pop(G)
    adj1 = "sneaky kleptomaniac"
    adj2 = "a pilfering pickopocket"
    title = f"{charfont}{name1} the Untrustworthy{o}"
    
if (choice == 3):
    char = "mod"
    charfont = f"\033[1m{B}"
    charfontw = f"{charfont}{[value for value in colours.values()][2]}\033[0m"
    colours.pop(B)
    adj1 = "charlatan imposter"
    adj2 = "a bit of a poser"
    title = f"{charfont}{name1} the Fraudulent{o}"

char1 = f"\033[1m{[key for key in colours.keys()][0]}"
char1w = f"{char1}{[value for value in colours.values()][0]}{o}"
char2 = f"\033[1m{[key for key in colours.keys()][1]}"
char2w = f"{char2}{[value for value in colours.values()][1]}{o}"
char3 = f"\033[1m{[key for key in colours.keys()][2]}"
char3w = f"{char3}{[value for value in colours.values()][2]}{o}"
char4 = f"\033[1m{[key for key in colours.keys()][3]}"
char4w = f"{char4}{[value for value in colours.values()][3]}{o}"
char5 = f"\033[1m{[key for key in colours.keys()][4]}"
char5w = f"{char5}{[value for value in colours.values()][4]}{o}"

#print(f"{char1}testing{o} {char2}different{o} {char3}character{o} {char4}colours{o}")
#print(f"In the {char1w} corner")
#print(f"In the {char2w} corner")
#print(f"In the {char3w} corner")
#print(f"In the {char4w} corner")
#print(f"In the {char5w} corner")

#🔔 
#🥊
def bell(a):
    global result, oppname, opptitle, corner
    if a == "start": 
        print (f"In the {charfontw} corner, we have {adj2} all the way from the arse end of nowhere, a {adj1}, {title}{charfont}!{o}")
        print(f"In the {corner} corner, we have {opptitle}{o}")
    time.sleep(5)
    for i in range (3):
        print("\n"*10)
        print(f"{' ':>{50}}🔔  ", end = "\r")
        time.sleep(0.5)
        print(f"{' ':>{49}}(🔔 )", end = "\r")
        time.sleep(0.05)
        print(f"{' ':>{46}}(  (🔔 )  )", end = "\r")
        time.sleep(0.06)
        print(f"{' ':>{43}}(  (  (🔔 )  )   )")
        print(f"\n{' ':>{49}}\033[1mDING")
        time.sleep(0.08)
        os.system("clear")
        if i == 2:
            print("\n"*10)
            print(f"{' ':>{50}}🔔  ")
            time.sleep(0.5)
            if a == "start":
                print(f"\n{' ':>{48}}\033[1mFIGHT!!!")
            elif a == "over":
                print(f"\n{' ':>{36}}{result}")
            time.sleep(1)
    os.system("clear") 

def boxing(n, opp, bonus):
    global result, char1, char1w, char2, char2w, char3, char3w, char4, char4w, char5, char5w, corner, opptitle
    if opp == "practice":
        if char == "fighter":
            oppname = "paper bag"
        else:
            oppname = "a stiff breeze"
    elif opp == "Ruth":
        oppname =  "Ruth Jenkins"
        corner = char3w
        opptitle = f"{char3}The Thunder from Down Under ... Ruth 'The Roo' Jenkins!!!{o}"
        # if successful - the Kangaroo Killer
    elif opp == "Bertha":
        oppname = "Big Bertha" 
        corner = char4w
        opptitle = f"{char4}Big Burly Bertha - The Big Burly Bear!!!{o}"
        # if successful - the Bear Basher
    elif opp == "Andrew":
        oppname = "Andrew The Giant"
        corner = char5w
        opptitle = f"{char5}The World's Biggest Little Person ... Andrew 'no relation' The Giant{o}"
        # if successful - the Giant 
    elif opp == "Father O'Connor":
        oppname = "Paddy O'Connor"
        corner = char1w
        opptitle = f"{char1}Older Than The Sport Itself ... Father 'Brittle Bones' O'Connor{o}"
        # if successful - the Priest Puncher 
    elif opp == "grandmother":
        oppname = "someone from the crowd's grandmother"
        corner = char4w
        opptitle = f"{char4}Banned from Bingo Halls Everywhere ... Delyth 'The Devastator' Davies{o}"
        # if successful - Granny Grappler
    elif opp == "Tyke":
        oppname = "Tyke Myson" #wait, did you just say - NO, I said TYKE MYSON, 
#known for 1st round knockouts, because he has to be home by 7 - why's that? - you'll see
        corner = char2w
        opptitle = f"{char2}The Meanest 10 Year Old You've Ever Seen ... Tyke 'The Terrible Tween' Myson{o}"
        # if successful - the 
        
    bell("start")
    punchlist = ['Cross!', 'Uppercut!', 'Haymaker!', "Jab!", "Left Hook!", "Right Hook!"]
    combo = [] # - list of commands shouted, must be kept outside the loop
    for i in range (n):
        command = random.choice(punchlist)  # i.e. Cross!
        print("\n"*11,f"{' ':>{45}}{command}")    # This is the coach shouting the command
        time.sleep(2)                       # make time shorter or longer depending on difficultty
        os.system("clear")
        punch = (f"{command[:1]}")          # i.e. C - making list of strikes the fighter must respond   
        
        # For 1 punch at a time
        #choice_punch = input("What did he say?")  ##single punch version
        ####single version                         ##single punch version
        #if choice_punch == punch.lower() or choice_punch == punch.upper():
         #   print("correct!")                      ##single punch version
        #else:                
         #   print("wrong!")     
         ##################################
         
         # for a long list of punches
        combo.extend([punch])
    landed = 0
    taken = 0
    knockout = 0
    if bonus == "bonus":
        rounds = n
    elif bonus == "nobonus":
        rounds = n+1
    # extra = n+1 ### way of asking for all punches together as an extra question at the end (otherwise put range(n) )
    for i in range (rounds):
        if i == 0: 
            a = "\nQuick! Think! What was the first punch?\n"
            
        ############ EXTRA BONUS QUESTION  - ALL PUNCHES TOGETHER
        elif i == n: ## remember, i only goes UP TO the number specified - having range 'extra' means 'n' is the last go of the loop
            if landed == (n):
                a = "\nWhat's all of the punches again?"
                print("".join(combo).lower())
                print(f"{' ':>{36}}{charfont}   🥊  🥊  🥊  -----------  🥊  🥊  🥊\033[0m", end = f"\r{' ':>{36}}{charfont}   🥊  🥊  🥊  --\033[1m")
                choice_punch = str(input())
                if choice_punch == "".join(combo).lower() or choice_punch == "".join(combo).upper() :
                    #fullname += tite (define 'title' variable depending on opponent, then finally 'heavyweight champion')
                    result =(f"And the winner is ...... {title}")
                else:
                    print("Watch out! WHAAAAAM!!!")
                    print("Ooof! You've been hit hard! You're flat out on the mat!")
                    result = (f"And the winner is {opponent} by knockout")
                break
            else: 
                
                knockout += 1
                break
        
        else:
            a = "\nWhat next?\n"
        print(a)
        print(f"{' ':>{36}}{charfont}   🥊  🥊  🥊  -----  🥊  🥊  🥊\033[0m", end = f"\r{' ':>{36}}{charfont}   🥊  🥊  🥊  --\033[1m")
        choice_punch = str(input())
        if choice_punch == combo[i].lower() or choice_punch == combo[i].upper() :
            print("\nCorrect!")
            landed += 1
            if landed == (n):
                result =("\nWhat a knockout! Superb! You won!!")
                
                #break
        else:                
            print("wrong!")
            taken += 1
            print(taken)
            #landed = 0 # start again, save for difficulty setting
            if taken == (n):  ## make number lower for harder difficulty, like n-1, 2, etc, n//2, n//3
                result = ("Ooof! You've been hit hard! You're flat out on the mat!")
                #break
        time.sleep(2)
        os.system("clear")
    time.sleep(2)
    os.system("clear")
    if knockout == 1:
        print("Watch out! WHAAAAAM!!!")
        result = (f"And the winner is {oppname}{o} by knockout") ## fill in opponent name variables later
    elif landed != n and landed > taken:
        result = ("You win by split decision")
    elif taken != n and  landed < taken:
        result = ("You lost by split decision")
    bell("over")

boxing(3, "Tyke", "nobonus")
