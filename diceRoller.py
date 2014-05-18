#Dice rolling program
#Aim is to roll a 6 or roll a number twice in a row

import random
import time

s1 = "- - - - -\n|       |\n|   O   |\n|       |\n- - - - -\n" #the dice prints
s2 = "- - - - -\n| O     |\n|       |\n|     O |\n- - - - -\n"
s3 = "- - - - -\n| O     |\n|   O   |\n|     O |\n- - - - -\n"
s4 = "- - - - -\n| O   O |\n|       |\n| O   O |\n- - - - -\n"
s5 = "- - - - -\n| O   O |\n|   O   |\n| O   O |\n- - - - -\n"
s6 = "- - - - -\n| O   O |\n| O   O |\n| O   O |\n- - - - -\n"

def roll(): #rolling a random number
    print("rolling.....\n")
    roll = random.randint(1,6)
    return roll

def show_dice(roll): #what that roll equates to - dice print
    if roll == 1:
        print(s1)
    elif roll == 2:
        print(s2)
    elif roll == 3:
        print(s3)
    elif roll == 4:
        print(s4)
    elif roll == 5:
        print(s5)
    elif roll == 6:
        print(s6)


def Until6(roll,show_dice):
    ask = input("Would you like to roll the dice? (y/n)")#give the user an option not to roll
    if ask == "y":
        myroll = roll()
        while myroll != 6: #if the roll isn't 6, keep going until it is
            time.sleep(1)
            show_dice(myroll)
    else:
        print(":(")

def UntilTwice(roll,show_dice):
    ask = input("Would you like to roll the dice? (y/n)")#give the user an option not to roll
    if ask == "y":
        myroll1 = 0 #creating both variables
        myroll2 = 1
        while myroll1 != myroll2: #while both rolls are different
            myroll1 = roll() #roll until both rolls are the same
            show_dice(myroll1)
            time.sleep(1)
            myroll2 = roll()
            show_dice(myroll2)
            time.sleep(1)
    else:
        print(":(")





    
