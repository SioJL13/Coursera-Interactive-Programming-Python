# Rock-paper-scissors-lizard-Spock template
import random

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def name_to_number(name):
    # delete the following pass statement and fill in your code below
    if(name == "Spock" or name=="spock" or name=="SPOCK"):
        return 1
    elif(name == "Rock" or name =="rock" or name=="ROCK"):
        return 0
    elif(name == "Paper" or name=="paper"  or name=="PAPER"):
        return 2
    elif(name == "Lizard" or name=="lizard" or name == "LIZARD"):
        return 3
    elif(name=="Scissors" or name=="scissors" or name=="SCISSORS"):
        return 4
    else:
        ##-1 means invalid number
        return -1

    # convert name to number using if/elif/else
    # don't forget to return the result!


def number_to_name(number):
    # delete the following pass statement and fill in your code below
    if(number == 0):
        return "Rock"
    elif(number == 1):
        return "Spock"
    elif(number == 2):
        return "Paper"
    elif(number == 3):
        return "Lizard"
    elif(number==4):
        return "Scissors"
    else:
        return "Invalid number"
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    

def rpsls(player_choice): 
    # delete the following pass statement and fill in your code below
    
    # print a blank line to separate consecutive games
    print ""

    # print out the message for the player's choice
    print "Player chooses: " + player_choice
    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)
    #print player_number
   
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0,5)
    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    # print out the message for computer's choice
    print "Computer chooses: " + comp_choice

    # compute difference of comp_number and player_number modulo five
    difference = (comp_number - player_number) %5
    #print difference

    # use if/elif/else to determine winner, print winner message
    if(difference == 1 or difference == 2):
        print "Computer wins!"
    elif(difference == 3 or difference ==4):
        print "Player wins!"
    else:
        print "Tie game!"

    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


