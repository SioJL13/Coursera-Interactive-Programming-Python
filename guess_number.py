# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random

secret_number=0
rangeNum = 100
lives = 0

# helper function to start and restart the game
def new_game():
    global secret_number
    global lives
    global rangeNum
    
    secret_number = random.randrange(0,rangeNum)
    
    if(rangeNum==100):
        lives = 7
    else:
        lives = 10
    
    print "New game. Range is set to 0 -",rangeNum
    
# define event handlers for control panel
def range100():
    global rangeNum
    rangeNum = 100
    new_game()

def range1000():
    global rangeNum
    rangeNum = 1000
    new_game()
    
def input_guess(guess):
    int_guess = int(guess)
    global secret_number
    global lives
    
    print "You picked: ",guess
    if(int_guess == secret_number):
        print "Correct!"
        new_game()
    elif(int_guess > secret_number):
        print "Lower"
        lives = lives - 1
        print "You have",lives,"chances left"
    else:
        print "Higher"
        lives = lives - 1
        print "You have",lives,"chances left"
    
    if(lives ==0):
        print "You lose the game. The number was:",secret_number
        print " "
        new_game()

    
# create frame
f = simplegui.create_frame('Guess the number',200,200,200)
f.add_button("Range: 0-100",range100)
f.add_button("Range: 0-1000",range1000)
f.add_input('Input',input_guess,50)


# register event handlers for control elements and start frame
f.start()

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
