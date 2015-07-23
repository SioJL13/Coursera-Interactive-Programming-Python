# Input comes from a mouse clicks.
# The implementation is very basic where the cards are just numbers from 0 to 9.

import simplegui
import random

# Global variables
CARDS = list()
TURN = 0
EXPOSED = list()
STATE = 0
INDEX_CARD1 = 0
INDEX_CARD2 = 0

# helper function to initialize globals
def new_game():
    global CARDS, TURN, EXPOSED
    CARDS = [i for i in range(8)]*2
    EXPOSED = [False] * 16
    random.shuffle(CARDS)
    TURN = 0

# define event handlers
def mouseclick(pos):
    global TURN, STATE, INDEX_CARD1, INDEX_CARD2, CARDS
    click_index = pos[0] // 50
    #print click_index
    if not EXPOSED[click_index]:
        EXPOSED[click_index] = True

        #State 0 corresponds to the start of the game
        if STATE == 0:
            STATE=1
            INDEX_CARD1 = click_index
        #State 1 corresponds to a single unpaired card
        elif STATE == 1:
            INDEX_CARD2 = click_index
            STATE = 2
        #State 2 corresponds to the end of the turn.
        #Here we need to check if the 2 exposed cards are equal
        else:
            if CARDS[INDEX_CARD1] != CARDS[INDEX_CARD2]:
                EXPOSED[INDEX_CARD2] = False
                EXPOSED[INDEX_CARD1] = False
            INDEX_CARD1 = click_index
            STATE = 1
        TURN += 1


# cards are logically 50x100 pixels in size
def draw(canvas):
    label.set_text("Turns = "+str(TURN))
    for i in range(16):
        canvas.draw_line([50*(i%15+1),0],[50*(i%15+1),100],2,"Blue")
        if EXPOSED[i]:
            card_pos = ([15+50*i,70])
            canvas.draw_text(str(CARDS[i]),card_pos,40,"RED")
    #for card_idx in range(len(CARDS)):
        #card_pos = (50 * card_idx,100)
        #canvas.draw_text(str(CARDS[card_idx]),card_pos,18,"RED")



# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric
