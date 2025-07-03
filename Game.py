import os 
import random



############################# MIDDLE ###########################################

def middle(m):
    print(f"{m}".center(101, " "))
    
np = f"{' ':>{5}}" #new paragraph 
nl = f"{' ':>{2}}" #new paragraph

########################### BORDERS ############################################
border = "-".center(100, "-")
deathborder = " \u2620  \u2620  \u2620  \u2620  \u2620  ".center(100, "x")
gameover = " \U0001F480   \U0001F480   \U0001F480   GAME OVER  \
\U0001F480   \U0001F480   \U0001F480  ".center(100, "~")

################################## VALIDATION ##################################
def getInput(a):
    if a == 2:
        b =  "  choose either 1 or 2"
    else:
        b = f"choose between 1 and {a}"
    while True:  
        try: 
            choice = int(input()) 
        except: 
            print(f"\n{' ':>{42}}\033[0m\033[1m\033[41m  Invalid input  \033[0m") 
            print(f"\n{' ':>{42}}\033[1mYou need a number \n{' ':>{36}}\033[2m(remember those from school??)\033[0m\033[1m  \n{' ':>{39}}{b}\033[0m") 
            ask()
            continue 
        if (choice <=0 or choice >a): 
            print(f"\n{' ':>{43}}\033[0m\033[1m\033[41m  Invalid input  \033[0m") 
            print(f"\n{' ':>{40}}\033[1mWell, that was a number \n{' ':>{36}}\033[2m  (but you ordered off menu)\033[0m\033[1m  \n{' ':>{39}}{b}\033[0m") 
            ask()
            continue 
        else: 
            print("\033[0m", flush=True, end = "\r")
            return choice

def strinput(a):
    if a == "yn":
        maybe = random.randint(1,5)
        if maybe == 1:
            b = f"'Y' for yes or 'N' for no \n{' ':>{42}}or 'M' for maybe"
        else:
            b = "'Y' for yes or 'N' for no"
    elif a == "leftright":
        b = f"a direction, \n{' ':>{31}}such as 'L' for left, 'R' for right...\
\n{' ':>{29}}\033[2m(or use your imagination and look up, down, \n{' ':>{26}}you can even look inside \
the eye of your mi-i-ind \n{' ':>{27}} but whatever you do, don't look back in anger)\033[0m"
    while True:  
        try: 
            choice = str(input()) 
        except: 
            print("\n\033[0m     \033[1m\033[41m    Invalid input  \033[0m")
            print(f"\033[1m      Please enter {b}") 
            ask(0)
            continue 
        if a == "yn":
            if choice.upper() == "Y" or choice.upper() == "N": 
                return choice
            elif choice.upper() == "M": 
                print(f"\n{' ':>{42}}\033[0m\033[1m\033[41m  Invalid input  \033[0m")
                print(f"\n{' ':>{36}}\033[1mThat was obviously a joke you \n{' ':>{32}}indecisive fence-sitting wet blanket! ") 
                ask()
                continue
            else: 
                print(f"\n{' ':>{42}}\033[0m\033[1m\033[41m  Invalid input  \033[0m")
                print(f"\n{' ':>{26}}\033[1m      Please enter {b}")
                ask()
        if a == "leftright":
            if choice.upper() == "L" or choice.upper() == "R" \
            or choice.upper() == "U" or choice.upper() == "D": 
                return choice
            else: 
                print(f"\n{' ':>{42}}\033[0m\033[1m\033[41m  Invalid input  \033[0m")
                print(f"\n{' ':>{38}}\033[1mPlease enter {b}")
                ask()

charfont = '\033[0m'
def ask(): 
    print(" ")
    print(f"{' ':>{36}}{charfont}   \u27B3  \u27B3  \u27B3 ------ \u27B3  \u27B3  \u27B3\033[0m", flush=True, end = f"\r{' ':>{36}}{charfont}   \u27B3  \u27B3  \u27B3  --\033[1m")


    
########################### INVENTORY  #########################################
#figure out, then put in status bar

#ideas
#scroll = "\U0001F4DC"
#rock = "\U0001FAA8"
#hcoin = '\033[33m\u25D6\033[0m'
#sword = "\U0001F5E1"
#disguise = "\U0001F978"
#ilist = []

#for n in ilist:
 #   print(n)
#addscroll = input("do you want to add a scroll to your inventory? Y/N")
#if addscroll == "Y":
 #   ilist.extend([scroll])
  #  print ("You have added ", (ilist[2]))
#elif addscroll == "N":
 #   print("You have decided not to take the scroll")
#print(' '.join(ilist))

############# New inventory approach, dictionary #######

# "sword":"\U0001F5E1", "Scroll":"\U0001F4DC", "disguise": "\U0001F978", "rock" : "\U0001FAA8"

idic = {}
# how to add to dictionary = idic.update({"disguise": "\U0001F978"})

def openi():
    global ichoice, usei
    while True:
        if len(idic) == 0:
            usei = 0
            break
        if len(idic) > 0:
            print("Would you like to look in your inventory? [Y/N]  ")
            choice =strinput("yn")
            if choice.upper() == "N":
                print("suit yourself")
                usei = 0
                break
            if choice.upper() == "Y":
                print("\n\033[2mRemember, your inventory is CASE SENSITIVE ... \
(meaning you carry your belongings in a sensitive case)\033[0m")
                options = []
                a =1
                for i in idic:
                    print(f"To use your  {idic[i]}   enter \033[1m{i[:1]}\033[0m")
                    #choice = getInput("opt") ###### - make getInput function that checks if choice is in options list
                    options.extend(i[:1])
                    a+=1
                    #print (" ".join(options))
                ichoice = input("What will you choose?:  ")
                if ichoice not in options:
                    print("invalid response")
                else:
                    usei = 1
                    return ichoice
def openiagain():
    if len(idic) > 1:
        print("You have other items.")
        openi()
    


########################### STATUS BAR #########################################
money = 5      #### did initially go with making only one status bar and 
#changing the wealth variable inside it (setting if >5, <=5 outside) but 
#it's a lot more hassle, go back to it after everything else is sorted
def status():
    global money, health
    if money > 5:
        print(border)
        print(" \033[31m\u2764 \033[0m "*health,"\u2764  " * (maxhealth-health),\
    "                      "," \U0001FA99  X",money,\
    "         ", " ".join(idic.values()))
       # print(drawScreen(health),purse(money))
        print(border) 
    else:
        print(border)
        print(" \033[31m\u2764 \033[0m "*health,"\u2764  " * (maxhealth-health),\
    "                "," \U0001FA99  " * money,\
    "                 ", " ".join(idic.values()))
       # print(drawScreen(health),purse(money))
        print(border) 

#status()
########################### HEADINGS  #######################################
def head(a):
    heading = a.center(100, " ")
    print(f"\n\033[1m{heading}\033[0m")
    
def headu(a):
    heading = a.center(100, " ")
    print(f"\n\033[1m\033[4m{heading}\033[0m")

#print(" \n \033[1m\033[4  ",  heading,"  \033[0m")
# example head("CHAPTER 1")

################### CHAPTER RECORD #########################
synopsis = " "
def chaptertxt(a):
    chapter = (f"Chapter {a}\n") 
    f = open("Chapters.txt","a")  
    f.write(chapter) 
    f.close()  

def synopsistxt(a):
    synopsis = (f"{a}\n\n")
    f = open("Chapters.txt","a")  
    f.write(synopsis)  
    f.close()
    
    
#chaptertxt("1")
#wealth = 5
#synopsistxt(f"It begins. You start with a wealth of {wealth} and full health")
#chaptertxt("2")
#wealth = wealth + 1
#synopsistxt(f"It continues. 2 You earnt a gold coin! You now have {wealth} gold coins")

########################### CONTINUE FUNCTIONS  ############################
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def cont(a):
    print(" ")
    if a == "j":
        print((" \u27B3 "*12).center(101, " "))
        input("  Press 'ENTER' to journey onwards  ".center(101, "-"))
        clear()
    elif a== "talk":
        print((" \U0001F444 ").center(101, " "))
        input(" Press 'ENTER' to continue the conversation ".center(101, "-"))
        clear()
    elif a== "pick":
        print((" \u270B ").center(101, " "))
        input(" Press 'ENTER' to pick it up ".center(101, "-"))
        clear()
    elif a== "look":
        print((" \U0001F50D ").center(101, " "))
        input(" Press 'ENTER' to look closer ".center(101, "-"))
        clear()
    elif a== "read":
        print((" \U0001F4D6 ").center(101, " "))
        input(" Press 'ENTER' to read more ".center(101, "-"))
        clear()
    elif a== "return":
        print((" \u23CE ").center(101, " "))
        input(" Press 'ENTER' to return ".center(101, "-"))
        clear()
    elif a== "fight":
        print((" ⚔️ ").center(101, " "))
        input(" Press 'ENTER' to begin fighting ".center(101, "-"))
        clear()
    
############################### Naming Function ################################

def namef(gerund, nick):
    global name, nickname, adj1, fullname
    nickname = f"{title}{charfont} {nick}{o}" 
    name = f"{name}" + f" {gerund},"
    fullname = f"{name[:-1]} {adj1}{o}"   #[:-1] takes away the last comma from the list

### EXAMPLE
#namef("bear killing", "bear killer")
#print(f"your current name is {nickname}.")  i.e. <Dewi the Violent Bear Killer>
#print(f"your full name is {fullname}.")     i.e. <Dewi the Violent Bear Killing Meatheaded Savage>
    
#################################################################################
###########################  INTRO (NAME AND QUEST ##############################
#################################################################################

headu( "IT BEGINS...")
name1 = input(f"\n{np}What is your name brave warrior?     ") 
print(f"\n{np}Welcome, \033[1m{name1}\033[0m")
while True:
    q1 = input(f"{np}Dare you venture on a quest? [Y/N]     ")
    if q1.upper() == "Y":
        print(f"\n{np}Splendid. Let's continue post haste")
        break
    elif q1.upper() == "N":
        clear()
        print(f"\n{np}Alright, bugger off then")
        raise SystemExit
    else:
        print(f"\n{np}Let's try that again shall we?")
        q2 = input(f"\n{np}DO YOU WANT TO GO ON A QUEST \033[1m{name1.upper()}\033[0m?! TYPE Y FOR YES, N FOR N     ")
        if q2.upper() == "Y":
            clear()
            print(f"\n\n{np}Splendid. \n\n{nl}You have finally mastered typing in one letter at a time.\
            \n{nl}Let's hope the only challenges you face are physical, not mental\n\n")
            break
        elif q2.upper() == "N":
            clear()
            print(f"{np}Alright, bugger off then")
            raise SystemExit
        else:
            clear()
            print(f"{np}Let's go through this again ... slowly ...")


cont("j")



############################## CHARACTER ###########################################
#Master of disguise armed with devilish disguise print("\U0001F978"), same everything else
#Fighter starts with 4 money, 6 health
#Thief starts with   6 money, 5 health

#conversation/character fonts
#making list and removing user defined character colour from list allows the other colours to be used 
#throughout the game, rather than taking up three colours during character level

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

headu("CHOOSE YOUR CLASS")
print(f"\n{np}How do you fancy yourself? \
\n{nl}[1] A strong, powerful {b}{R}fighter?{o}  \n{nl}[2] An agile and stealthy {b}{G}thief?{o} \
\n{nl}[3] Or a {b}{B}master of disguise?{o} ")
choice = getInput(3)

if (choice == 1):
    char = "fighter"
    charfont = f"\033[1m{R}"
    charfontw = f"{charfont}{[value for value in colours.values()][0]}\033[0m"  #designates colour word in colour
    colours.pop(R)  # deletes item from list whilst keeping the variable value (unlike from 'del')
    adj1 = "meatheaded savage"
    adj2 = "an aggressive brute"
    title = f"{charfont}{name1} the Violent\033[0m"
    name = f"{charfont}{name1} the Violent"
        
if (choice == 2):
    char = "thief"
    charfont = f"\033[1m{G}"
    charfontw = f"{charfont}{[value for value in colours.values()][1]}\033[0m"
    colours.pop(G)
    adj1 = "sneaky kleptomaniac"
    adj2 = "a pilfering pickopocket"
    title = f"{charfont}{name1} the Untrustworthy\033[0m"    
    name = f"{charfont}{name1} the Untrustworthy"
    
if (choice == 3):
    char = "mod"
    charfont = f"\033[1m{B}"
    charfontw = f"{charfont}{[value for value in colours.values()][2]}\033[0m"
    colours.pop(B)
    adj1 = "charlatan imposter"
    adj2 = "a bit of a poser"
    title = f"{charfont}{name1} the Fraudulent\033[0m"
    name = f"{charfont}{name1} the Fraudulent"
    
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

print(f"{np}Ah, so you're a {adj1} I see.\n\n{nl}You shall henceforth be known across \
the kingdom as {title}\033[0m.")

          # ------------ CHARACTER STATUS  --------------------#

if char == "mod":
    health = 5
    maxhealth = 5
    money = 3
elif char == "fighter":
    health = 7
    maxhealth = 7
    money = 1
elif char == "thief":
    health = 5
    maxhealth = 5
    money = 7
    
cont("j")
status()
print("\n")
if char == "fighter":
    print(f"As a big strong {adj1}, you have more health than the average person.\n\nHowever, \
as you spent most of our life savings on protein powder, you only have 1 gold coin to your name")
elif char == "thief":
    print(f"Being a {adj1}, you traded your grandmother's jewellery at the local \
converters of cash \nbefore this quest began. You have an abundance of riches (and absolutely no shame).")
if char == "mod":
    print(f"As a {adj1}, you are of average health and wealth (in other words, pretty vanilla), \
\nhowever there is one interesting thing about you ... you carry a devilish disguise. \
\n\nWith this ingenious and uncannily lifelike cloak of anonymity, no one will ever see the real you underneath.")
    input("Press 'ENTER' to see your masterful disguise. \n\n")
    print(" \U0001F978 ".center(100, " "))
    print("\nThis shall be added to your inventory")
    idic.update({"disguise": "\U0001F978"})
print("")

def changehealth(a,b):
    global health, maxhealth
    increase = maxhealth - health
    if a <1:
        health += a
        middle(b)
        if health > 0:
            print("\033[1m")
            middle(f"YOU LOSE {a} HEALTH.")
            print("\033[0m")
        elif (health <=0): 
            print("You have lost all your health. \nYou cease to be, and shall be \
    remembered by only the few unlucky enough to have known you as", name,".\n \
    There will be no funeral for you.\nYour life, much like this game, is over.\n")
            print(deathborder)
            print(border)
            print(gameover) 
            print(border)
            print(deathborder) 
            raise SystemExit
    elif health == maxhealth:
        middle("You're already at your maximum health level.")
        middle("If anything you can afford to smoke a few cigars, fight a bear or two")
        middle("... maybe just one bear")
    else:
        health += a
        middle(b)
        if health < maxhealth:
            print("\033[1m")
            middle(f"YOU GAIN {a} HEALTH.")
            print("\033[0m")
        if health >= maxhealth:
            health = maxhealth
            if increase == a:
                asand = "and thus"
            if increase < a:
                asand = "only, as"
            print(f"You gained {increase} health {asand} you have reached your maximum level. \
\nYou're as healthy as can be. What a fine specimen you are.")

        
# example, eat mushroom gain 1 HEALTH
#maxhealthf(1, "That was a wise decision, you feel bigger, stronger. ")

############################### HEALTH ####################################

def drawScreen(health): 
    print(border) 
    print("\033[31m\u2764 \033[0m "*health,"\u2764  " * (maxhealth-health)) 
    print(border) 

########################### WEALTH ############################################
def purse(money): 
    print(border) 
    print("\U0001FA99  " * money) 
    print(border) 
    
# call function --> drawScreen(wealth)

#################################################################################
################################ CHAPTER 1 ######################################
#################################################################################

cont("j")
clear()
head("CHAPTER 1")
status() 
print(f"\n\n     You, the one they call {title}, walk onwards. \
\n\n   You come to a fork in the road. A decision must be made.\n\n")
cont("read")
status()
print("\n\n     One path is clear and flanked with lush green grass, tall mighty trees that home \
\n   singing sparrows and sumptuously succulent fruit ripe for the picking. High above it is a \
\n   bright blue sky adorned by a glorious shining sun.\
\n\n   The birds melody will surely ease you along your journey and your belly yearns for the \
\n   nourishment of fresh plump fruit. \
\n\n   This path promises a joyous and tranquil trek to your destination, whereas the other path...")

cont("read")
status()
print("\n\n     This second path is dark and gloomy. \n\nIt is surrounded by dead grass, a dark and foreboding storm cloud\
rains down upon it, \nthe crack of lightning briefly illuminates the dangerously unkempt trail.\
\n\nHowever, before you have time to question how such two such distinctly different weather climates\
\ncan exist so close to each other, a peculiar sight catches your eye...")

cont("read")
status()

print("\n\n     You spy, proudly fastened to a closed fence, a curious crest of crimson  \
decorated with \na simple and elegant emblem, a single brilliant white stripe. \n\nBeing merely" ,adj2,"from \
a bog infested swamp, you have before never seen such beauty. \n\nIt may just be the bright shiny colour,\
but this sign calls to you. \
\n\nWhich of these options looks more promising?\n")

input("  Press 'ENTER' to compare the paths  ".center(101, "-"))
clear()
for i in range(1):
    while True:
        print(f"\n\n{' ':>{32}}{b}                       {BK}     __")    
        print(f"{' ':>{32}}{G}  _           (🐦 ){BK}      ___(__)___  ")
        print(f"{' ':>{32}}{G}  ~ )   {o}{Y}\u2600{b}  {G} ( ~  ~ ){BK}   (___)_)_)__) ")
        print(f"{' ':>{32}}{G} ~ ~ )     ( ~ ~ ~ ~){BK}  (___)__)_)  ")
        print(f"{' ':>{32}}{G}  ~ ~ )   ( ~ ~  ~ ~ ){r} {B} '''{Y}_/{B}''    ")
        print(f"{' ':>{32}}{G}  ~ ~ )   ( ~ ~  ~ ~ ){r} {B} ''{Y}/ {B}''     ")
        print(f"{' ':>{32}}{G}  ~ ~)     ( ~ ~ ~ ~){r}    {B}'' {B} ''{o}    ")
        print(f"{' ':>{32}}   -        --| ~|--    ''         ")
        print(f"{' ':>{32}}  |___     _🦜_|6 |                 ")
        print(f"{' ':>{32}}  | 🍎🍏    🍎   | \|       [=]        ")
        print(f"{' ':>{32}}  |           |\ |        ¦         ")
        print(f"{' ':>{32}}  |     ____  |  |  ____  ¦         ")
        print(f"{' ':>{32}}{b}{G}MMMMMMM{o}/----\{b}{G}MMM{BK}XXX{o}/----\{BK}XXXXXXXXXX")
        print(f"{' ':>{32}}{b}{G}MMMMMM{o}/------\{b}{G}MM{BK}XX{o}/------\{BK}XXXXXXXXX")
        print(f"{' ':>{32}}{b}{G}MMMMM{o}/--------\{b}{G}M{BK}X{o}/|==⛔ ==|\{BK}XXXXXXXX")
        print(f"{' ':>{32}}{b}{G}MMMM{o}/----------\/-|------|-\{BK}XXXXXXX")
        print(f"{' ':>{32}}{b}{G}MMM{r}/------------------------\{o}{BK}XXXXXX")
        print(f"{' ':>{32}}{b}{G}MM{r}/ _ _ _ _ _ _ _ _ _ _ _ _ _\{o}{BK}XXXXX{o}")
        print(f"{' ':>{32}}")
    ######## make cont function with "enter to return here" or something like that
    ######## make choice function with directions
        if i == 0:
            print("You must look up close at this glorious sign.")
            cont("look")
            print("\n\n")
            middle("⛔   " ) 
            middle("")
            middle("Such exotic, unfamiliar beauty.")
            middle("This is truly the work of a master craftsman, surely it belongs to a noble house.")
            middle("")
            middle("Such lavish adorenment signals that this path must be paved with gold.")
            middle("Obviously not literally, it's mostly mud and a slightly worrying amount of dung.")
            middle("")
            middle("Nevertheless, this is an auspicious sign to be sure.")
            middle("")
            middle("  Press 'ENTER' to take a step back and compare paths again  ")
            middle("       \033[2mAlthough it's barely a hard choice anymore\033[0m")
            input("")
            i += 1
            clear()
        elif i == 1:
            print("You must choose to go left [L] or right[R]. \
        \nThere are other options, like up or down, but they won't get you anywhere fast.")
            choice = strinput("leftright")
            clear()
            if choice.upper() == "L":
                status()
                print("\n\nAre you sure? Taking the safe, easy choice rather than the path less travelled? \
        \nYou don't seem to have the keen taste for risk and adventure that is necessary for risky adventures. \
        \nStill, up to you ... wait, there's another sign on the right path! Surely you must look?\n")
                i += 3
                break
            elif choice.upper() == "R":
                status()
                print("\n\nA brave choice indeed! Who needs sun, fresh fruit and safety when there are memories to be made? \
        \n\nThere appears to be a sign underneath further along the path.\n")
                i += 3
                break
            elif choice.upper() == "U":
                print("")
                print("")
                print("          \033[44m                                                           \033[0m")
                print("          \033[44m                                                           \033[0m")
                print("          \033[44m                                                           \033[0m")
                print("          \033[44m                                                           \033[0m")
                print("          \033[44m                                                           \033[0m")
                print("          \033[44m                                                           \033[0m")
                print("          \033[44m                                                           \033[0m")
                print("          \033[44m                                                           \033[0m")
                print("          \033[44m                 You see a pretty blue sky.                \033[0m")
                print("          \033[44m          It's very nice, but your neck is exposed         \033[0m")
                print("          \033[44m     and you have a rather large blind spot as far as      \033[0m")
                print("          \033[44m             land based threats are concerned.             \033[0m")
                print("          \033[44m     This is not a tactically advantageous position.       \033[0m")
                print("          \033[44m    Also, you have more important things to get on with.   \033[0m")
                print("          \033[44m                                                           \033[0m")
                print("          \033[44m                                                           \033[0m")
                input("                         Press 'ENTER' to look back down                     ")
                clear()
            
            elif choice.upper() == "D":
                print("                                                                     ")
                print("                            You look down at your shoes.                     ")
                print("           The creases at the front remind you of your shameful secret,      ")
                print("     you're a size 8 but insisted to the saleswoman you were 9 and a half.   ")
                print("                    But now is not the time for self reflection.             ")
                print("\033[0;33m                                                                   ")
                print("                        ________                 ________                    ")
                print("                       /        \               /        \                   ")
                print("                      /          \             /          \                  ")
                print("                     /    ^^^^    \           /    ^^^^    \                 ")
                print("                    /              |         |              \                ")
                print("                    |              |         |              |                ")
                print("                    |              /         \              |                ")
                print("                    |             |           |             |                ")
                print("                    |             |           |             |         \033[0m")
                input("                         Press 'ENTER' to look back up                     ")
                clear()

cont("look")
print("\n\n")
middle("                \033[40m\033[30m  \033[0m      ")
middle("              \033[1m\033[47m\033[30m  NO ENTRY  \033[0m")
middle("              \033[1m\033[47m\033[30m   BEARS!   \033[0m")
middle("                \033[40m\033[30m  \033[0m      ")
middle("                \033[40m\033[30m  \033[0m      ")
middle("                \033[40m\033[30m  \033[0m      ")
middle("                \033[40m\033[30m  \033[0m      ")

print("\n\nWell, this sign seems pretty anti-bear. \nStill, this path should at least be \
a litte safer if they're not allowed to enter\n")

cont("j")
status()

print("\n\nSuddenly, without any warning at all, a bear appears in front of you.\
\nThis shocking turn of events couldn't have been predicted. \nYou have an important choice to make. \
Enter:\n1. run\n2. fight") 
choice = getInput(2) 
clear()
if (choice == 1):#run 
    findsword = 1
    print("\n")
    middle("That was wise. Of course you can't fight a bear.")
    middle("You shall henceforth be remembered for your cunning tactical prowess.") 
    print("\n")
    middle("You're certainly cleverer than that bear, that's for sure.")
    namef("Bear Dodging", "yet Careful Bear Dodger") 
elif (choice == 2):#fight 
    #health = health - 4
    #drawScreen(health) 
    findsword = 0
    openi()
    if usei == 1:
        if ichoice == "d":
            os.system("clear")
            print("\n\033[1m")
            middle(f"You chose a disguise.")
            print("\033[0m")
            middle("Were this a Halloween party, it might provide useful.")
            middle("Maybe if you were up against another foe it could distract them.")
            print("")
            middle("   However, your current enemy doesn't seem to care \033[1mwho\033[0m you are,")
            middle("only that you have soft fleshy parts and snappable bones")
            print("")
            cont("read")
    namef("Bear Fighting", "and Foolish Bear Fighter")
    print("\n\n")
    middle("What, fight a bear? Who do you think you are? Jackie Chan?")
    middle("          \033[2m(He exists in this universe too) \033[0m")
    middle("That was very unwise.")
    middle("You lose 4 health, your right arm and half your face")
    middle("along with your common sense apparently)")
    middle("but you should count yourself bloody lucky!")
    changehealth(-4, "Your stupidity is now known across the land.")
    middle("At least you're not as stupid as that bear.")
middle("It didn't even read the sign. What an idiot.")
print("")
cont("j")
if findsword == 1:
    print("\n\nAs you keep running, in a not at all cowarldy way, you trip \
over an object hidden in the grass.")
    cont("look")
    print("\n\n")
    middle("       ,       ")
    middle("      / \      ")
    middle("     / | \     ")
    middle("     | | |     ")
    middle("     | | |     ")
    middle("     | | |     ")
    middle("     | | |     ")
    middle("     | | |     ")
    middle("     | | |     ")
    middle("  |\_|___|_/|  ")
    middle("  \_ _ _ _ _/  ")
    middle("      | |      ")
    middle("      | |      ")
    middle("       V       ")
    middle("")
    middle("It's a sword!")
        
    idic.update({"sword":"\U0001F5E1"})
    cont("pick")
    status()
    print("\n\n\033[1m")
    middle("You now have a sword!")
    print("\033[0m\n")
    cont("j")

elif findsword == 0:
    print("")
    middle("As you walk away, licking your wounds")
    middle("(the state you're in, that's gonne be a lot of lickin')")
    middle("You can't help but feel the heavy weight of something embedded deep within your chest")
    middle("")
    middle("You assume it's just regret for thinking you could take on a bear,")
    middle("but this is less of an emotional abstract pain")
    middle("and more of a tactile 'Ouch it's touching my lungs pain'")
    middle("")
    middle("It's a rock!")
    middle("It must have got in there one of the (many) times")
    middle("the bear slammed you down on the ground ")
    idic.update({"rock":"\U0001FAA8"})
    cont("pick")
    status()
    print("\n\n\033[1m")
    middle("You now have a rock!")
    print("\033[0m\n")
    middle("The bear might have taken your dignity, some extermities and a vital amount of blood,")
    middle("but as least you now have a rock and some life experience!")
    middle("See? Every cloud has a silver lining.")
    cont("j")
    

########################### CHAPTER 2 ############################################
head("CHAPTER 2")
status()
print("After your encounter with the bear, you, ", nickname, \
", \nstop for a rest. You notice in front of you a flask on the ground. \
\nDrinking from a random bottle you found on the ground is such a stupid thing to do, \
it's not even worth considering ...  \n\nEnter:\n1. drink from it\n2. leave it alone") 
choice = getInput(2) 
clear()
print("\n")
def poison(a):
    print("\n")
    middle("                   \033[1m\033[47m\033[30m               \033[0m")
    middle("                   \033[1m\033[47m\033[30m  BEAR POISON  \033[0m")
    middle("                   \033[1m\033[47m\033[30m       \U0001F571       \033[0m")
    middle("                   \033[1m\033[47m\033[30m DO NOT DRINK! \033[0m")
    middle("                   \033[1m\033[47m\033[30m               \033[0m")
    print("\n")
    if a == 1:
        middle("Ah, bad luck. You really should start reading things more carefully.")
        print("")
    elif a == 2:
        middle("Wait, does that mean it's only poisonous to bears?")
        middle("Hmmmmm ...")
        middle("Better not risk it")
        print("")
        
if (choice == 1):#drink 
    print("Well, you didn't get this far in life by \033[1mnot\033[0m drinking strange fluids. Here goes...\n\n")
    middle("\033[1mGlug glug glug\033[0m")
    print("\nOh wait there's a label on the other side, you should have probably checked that first ...")
    cont("look")
    poison(1)
    cont("return")
    namef("greedy poison drinking", "greedy poison drinker")
    print("\n\n")
    changehealth(-2, "That was unwise, drinking bear poison is not medically advised for humans (or bears).") 
elif (choice == 2):#leave alone 
    print("It's tempting, but you've probably made the right choice. You'll just never know for sure though.")
    print("\nOh wait there's a label on the other side, you should have probably \
checked that first ...\n")
    cont("look")
    poison(2)
    namef("wisely poison declining", "wise poison decliner") 
    middle('That was a wise choice. Poison has never agreed with your stomach.') 

cont("j")

########################### CHAPTER 3 ############################################ 
head("CHAPTER 3")
status()
print("\nYou see a knight in black armour, he is a mere stump on the ground. \
\nHe has lost his limbs and is bleeding profusely. Clearly a mighty battle ensued. \
\n\nMiraculously, he is still alive, between bouts of gargling his own blood he manages to ask ... \
\n\n\033[1mYou there! What is your name?\033[0m")

cont("talk")
print("\n\nYou only get one chance to make a first impression. Decide how you want to present yourself.\
\nEnter :\n1. Be kind and gracious \n2. Show that lump of rotting flesh who's boss ") 
choice = getInput(2)
os.system("clear")
if choice == 1:
    knight = f"{char1}Brave wounded soldier:\033[39m"
    print(f"\n\n{charfont}You\033[39m: I am but a humble traveller, I go simply by {charfont}{name1}\033[0m")
    print(f"\n{knight} Really? Is that all?\033[0m\n")
    cont("talk")
    print(f"\n\n{charfont}You\033[39m: Well, ahem, I'm not one for fancy titles or such regality, \
but I suppose you could call me \n{nickname}. \n\033[1mYou appear gravely wounded. Can I be of any assistance?")
    print(f"\n\n{knight} Help? My dear boy, you insult me, 'tis but a mere flesh wound.\033[0m")
    print("\n\nShould you help him regardless or carry on? \nEnter :\n1. Help \n2. Ignore") 
    choice = getInput(2) 
    clear()
    if (choice == 1):#help 
        namef("and stubbornly helpful but some say patroinising", "stubbornly helpful but some say patroinising")
        print("You bend down to pick him up, he calls you a patronising scoundrel and \
headbutts you!\n Ouch! You kick him off the road!")
        changehealth(-1, "You stubbed your toe on Sir Bleedsalot armour.")
    elif (choice == 2):#leave alone 
        namef("respectfully unhelpful", "and respectfully unhelpful")
        print("Fair enough, nothing you could do for him really. You continue with all your\
health intact (which is more than can be said for him)") 
elif choice == 2:
    knight = f"{char1}Talking stump on the ground:\033[39m"
    print(f"\n\n{charfont}You\033[39m: You may address me by my full title, \n{fullname}.\n\033[1mAnd who might you be? Sir Bleeds-a-lot?")
    print(f"\n{knight} Why you little ... come here! I'll give you a thrashing of a lifetime!\033[0m")
    cont("fight")
    print("\n")
    middle("What enues is an surprisingly fraught and close battle.")
    middle("For a fellow with no arms or legs, he's unpredictably nimble.")
    middle("He's certainly got you beat in the agility department,")
    middle("and what he lacks in limbs he makes up for in tenacity.\n\n")
################### possibly have to make dictionary for inventory, with symbols but also quick keys , like S for sword
#inventory approaches, 
#[1] as below, going through each possible item, 'if' statement to see if it's there
#[2] in screenshot, check if inventory is populated ("if inventory:) then cycling through objects with 'for i in list' loop
#[3] dictionary, may have to do this in order for [2] to work anyway !!!possible alternative - (ORRR first letter of i)!!!

    openi()
    if usei == 1:
        if ichoice == "r":
            print("This won't do anything, he's covered in armour. ")
            openiagain()
        if ichoice == "s":# This is fine for now but when there are too many items use plan B
            print("Would you like to use your sword? Enter [Y/N]\n.")
            choice = strinput("yn")
            if choice.upper() == "Y":
                print("Sure, that's what it's there for.")
                os.system("clear")
                print("\n\n")
                middle("You swing your mighty sword ... it's actually quite heavy.")
                middle("")
                middle("Somehow this legless warrior manages to dodge and weave your strikes,")
                changehealth(-1, "You drop your sword onto your foot.")
                print("You should seriously consider fighting lessons.")
                openiagain()
                usei = 0
            if choice.upper() == "N":
                print("I couldn't possibly, it'd be too unfair.")
                time.sleep(1)
                openiagain()
                os.system("clear")
                usei = 0
        if ichoice == "d":
            print("Would you like to use your disguise? Enter [Y/N]\n.")
            choice = strinput("yn")
            if choice.upper() == "Y":
                print("Sure, it's bound to work better on him than a bear.")
                os.system("clear")
                print("\n\n")
                middle("You run around a tree and don your disguise.")
                middle("The knight hops around the other side of the tree ... ")
                print(f"\n\n{knight} Come back you fiend! I'll bite you limb from ... Oh, I'm sorry. \
\n Pardon me my good Sir, have you seen a young rapscallion here in need of a good headbutt?.\033[0m")
                print("\nBeing a master of disguise, you must respond in a different accent from your own. \
\nEnter \n[1] Scottish \n[2] Chinese ")
                choice = getInput(2)
                if choice == 2:
                    os.system("clear")
                    print("\n")
                    print("\nYou clear your throat ... and decide it's probably best to revert to Scottish")
                if choice == 1 or choice == 2:
                    print(f"\n{charfont}You\033[39m: Ochayehesbeenaboootwhyhastheresbeenamurrrderbdkh2ebkxx3x?!@$")
                    print("")
                    middle("Confused, the knight bids you good day and bounces away")
                
                
    if usei == 0:
        if char == "fighter":
            print("")
            middle("This guy's proving to be a real challenge, imagine just how tough he'd be fully intact.")
            middle(f"However, being {adj2}, you manage to pick him up and fling him into some shrubbery where he belongs.")
            middle("You bested a limbless veteran on death's door.")
            middle(f"Your reputation as a {adj1} survives another day.")
        
            middle("You hate to say it, but you may have met your match.")
    
    






cont("j")

########################### CHAPTER 4 ############################################
head("CHAPTER 4")
status() 
print("In the middle of the path, they who go by moniker", nickname, "\
find a single large mushroom. It looks appetising,\
but you've been warned about picking strange mushrooms.\
Do you eat it, or ignore? Enter:\n1. Eat\n2. Ignore") 

choice = getInput(2) 
clear()
if (choice == 1):#eat 
    namef("mighty mushroom munching", "mighty mushroom muncher")
    changehealth(1, "That was wise. You grow bigger, and you feel stronger.")
    print(f"You shall henceforth be known as {nickname}.")
    
    #else: 
     #   print("That was wise. You grow bigger and bigger, you feel stronger.\
      #  You are now", name,"\nYet you are as healthy as can be. No extra health for you") 
elif (choice == 2):#ignore 
    drawScreen(health) 
    namef("flimsy fungi fearing", "yet flimsy fungi fearer")
    print("You,", nickname, "ignore the mushroom, walking onwards. You'll never know what dangers, or powers, it holds") 
cont("j")

print(fullname)
