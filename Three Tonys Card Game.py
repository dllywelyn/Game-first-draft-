import random
import time 
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
##  NEED TO WORK OUT HOW TO SHOW PICTURE CARD, i.e. 'J' BUT HOLD TRUE VALUE (11)
deck = ["2","2","2","2","3","3","3","3","4","4","4","4","5","5","5","5","6","6","6","6","7","7","7","7",
"8","8","8","8","9","9","9","9","10","10","10","10","J","J","J","J","Q","Q","Q","Q","K","K","K","K",
"A","A","A","A"]

# SOLUTION - Dictionary for values
dic = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":-10, "Q":0, "K":0, "A":11}

def rnd():
    print("\033[1m    Round", rounds)
    print ("\033[2m","  ".join(hand1),"\033[0m\n")
    
def ace(a,b):
    if a == "A":
        if "high" in b:
            dic[a] = 21
        elif "low" in b:
            dic[a] = 0
    
#def shuffle():
#players = int(input("How many players? 1-4:   "))
#for i in range (0,3): 
#for player in range (0, players):
 #   card = (random.choice(pickuppile))
  #  hand = []
   # handname = hand(f"{player}") 
  #  hand.append(card)
   # pickuppile.remove(card)
    #print (hand)
#print(pickuppile)
hand1 = []
hand2 = []
hand3 = []
hand4 = []

#players = int(input("How many players? 1-4:   "))
#for i in range (0,3):
####################   SHUFFLE ####################
for cards in range (0, 5):
    card1 = (random.choice(deck))
    hand1.append(card1)
    deck.remove(card1)
    card2 = (random.choice(deck))
    hand2.append(card2)
    deck.remove(card2)
    card3 = (random.choice(deck))
    hand3.append(card3)
    deck.remove(card3)
    card4 = (random.choice(deck))
    hand4.append(card4)
    deck.remove(card4)

for cards in range (0, 6):
    
    print ("Player 1 has    \033[1m", flush=True, end = "")
    print("    ".join(hand1[0:cards]),"\033[0m")
    print ("Player 2 has    \033[1m", flush=True, end = "")
    print("    ".join(hand2[0:cards]),"\033[0m")
    print ("Player 3 has    \033[1m", flush=True, end = "")
    print("    ".join(hand3[0:cards]),"\033[0m")
    print ("Player 4 has    \033[1m", flush=True, end = "")
    print("    ".join(hand4[0:cards]),"\033[0m")
    time.sleep(0.3)
    if cards == 5:
        time.sleep(2)
    clear()
print("\nRemember, \033[1mJacks\033[0m will \033[4mtake away 10\033[0m from the total,\
\n\n\033[1mQueens\033[0m will \033[4msplit\033[0m the total in half, \
\n\n\033[1mKings\033[0m will \033[4mdouble\033[0m it, \
\n\n\033[1mAces\033[0m can go \033[4mhigh or low\033[0m")

input(f"Press \033[1m[ENTER]\033[0m to continue".center(101, " "))
clear()

#print(pickuppile) 
wins = 0
p2wins = 0
p3wins = 0
p4wins = 0
#################   PLAY A ROUND ############################
for rounds in range (1, 6):
    rnd()
    possibilities = ["high even", "high odd", "low even", "low odd"]
    pdic = {"high even":"an even number above 23", "high odd":"an odd number from 23 and up", "low even":"an even number under 23", "low odd":"an odd number under 23"}
    yourtarget = random.choice(list(pdic))
    print("You pick a piece of paper. \nYou turn it over to reveal ... \033[1m\033[31m",yourtarget,"\033[0m")
    print(f"The total of all cards drawn must be \033[4m{pdic[yourtarget]}\033[0m for you to win")
    pdic.pop(yourtarget)
    p2target = random.choice(list(pdic))
    pdic.pop(p2target)
    p3target = random.choice(list(pdic))
    pdic.pop(p3target)
    p4target = random.choice(list(pdic))
    #print(f"Your target is {yourtarget}     player 2 has {p2target}     player 3 has {p3target}     player 4 has {p4target} ")
    play = input("Your turn. Which card would you like to play:  ")
    play = play.upper()
    if play in hand1:
        hand1.remove(play)
    if play == "A":
        acechoice = input("You have played an Ace. It's face value is 11, but you can choose to make it worthless or \
add an extra 10 to the total. \n Would you like to go high [H] or low[L]?")
        if acechoice.upper() == "H":
            dic[play] = 21
        elif acechoice.upper() == "L":
            dic[play] = 0
    table = []
    table.append(play)
    #print("You have remaining:","  ".join(hand1))
    #print(table,"is on the table")
    
    play2 = (random.choice(hand2))
    hand2.remove(play2)
    ace(play2,p2target)
    table.append(play2)
    #print("Player 2 has:",hand2)
    #print(table,"is on the table")
    
    play3 = (random.choice(hand3))
    hand3.remove(play3)
    ace(play3,p3target)
    table.append(play3)
    #print("Player 2 has:",hand3)
    #print(table,"is on the table")
    
    play4 = (random.choice(hand4))
    hand4.remove(play4)
    ace(play4,p4target)
    table.append(play4)
    #print("Player 2 has:",hand4)
    clear()
    print("On the table we have ... ")
    #put middle function here
    print("\033[1m", "  ".join(table),"\033[0m")
    total = (dic[play]+dic[play2]+dic[play3]+dic[play4])
    if "Q" in table:
        countQ = table.count("Q")
        total = total//(2*countQ)
    if "K" in table:
        countK = table.count("K")
        total = total*(2*countK)
    print ("Which makes the total ... \033[1m")
    print(f"{total}".center(101, " "))
    if total%2 == 0:
        oddeven = "even"
    else:
        oddeven = "odd"
    if total >= 23 and oddeven == "even":
        print("high and even!")
        result = "high even"
    elif total >= 23 and oddeven == "odd":
        print("high and odd!")
        result = "high odd"
    elif total < 23 and oddeven == "even":
        print("low and even!")
        result = "low even"
    elif total < 23 and oddeven == "odd":
        print("low and odd!")
        result = "low odd"
        
    if result == yourtarget:
        print("\033[1m\033[31mYou\033[0m are the winner!")
        wins = wins + 1
        print (f"your score is now {wins}")
    elif result == p2target:
        print ("\033[1m\033[32mPlayer 2\033[0m wins!")
        p2wins = p2wins+1
    elif result == p3target:
        print ("\033[1m\033[33mPlayer 3\033[0m wins!")
        p3wins = p3wins+1
    elif result == p4target:
        print ("\033[1m\033[34mPlayer 4\033[0m wins!")
        p4wins = p4wins+1
        
    
    input(f"Press \033[1m[ENTER]\033[0m to continue".center(101, " "))
    clear()

print (f"\033[1m\033[31mYour\033[0m score is {wins}")
print(f"\033[1m\033[32mPlayer 2\033[0m has {p2wins}, \033[1m\033[33mPlayer\033[0m 3 has {p3wins}, \
\033[1m\033[34mPlayer 4\033[0m has {p4wins}")
#change from wins >= 2 means you win because it is possible someone else could have 3
if wins > p2wins and wins > p3wins and wins > p4wins:
    print("Well done, you've won the game!")
elif wins == 1:
    print("Close but no cigar!")
elif wins == p2wins or wins == p3wins or wins == p4wins:
    print("It's a tie! Split pot!")
else:
    ("You didn't win a single round!")

    
    
    

    
    
