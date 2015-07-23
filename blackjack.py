# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
            card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank),
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
            canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
# define hand class
class Hand:
    def __init__(self):
        #list of cards
        self.player_hand = list()

    def __str__(self):
        info = "Hand contains "
        for card in self.player_hand:
            info += str(card) + " "
        return info

    def add_card(self, card):
        self.player_hand.append(card)

    def get_value(self):
        value = 0
        for card in self.player_hand:
            rank = card.get_rank()
            value = value + VALUES[rank]
        for card in self.player_hand:
            rank = card.get_rank()
            if rank == 'A' and value <= 11:
                value += 10
        return value

    def draw(self, canvas, pos):
        p = pos
        for card in self.player_hand:
            card.draw(canvas, p)
            pos[0] = pos[0] + 90
        if in_play == True:
            canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [115.5,184], CARD_BACK_SIZE)

# define deck class
class Deck:
    def __init__(self):
        self.cards = list()
        self.shuffle()
        for temp in SUITS:
            for temp2 in RANKS:
                card = Card(temp,temp2)
                self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        deal = self.cards.pop(0)
        return deal

    def __str__(self):
        info = "Hand contains "
        for card in self.cards:
            info += str(card) + " "
        return info



#define event handlers for buttons
def deal():
    global outcome, in_play, player, dealer, deck, score

    deck = Deck()
    deck.shuffle()

    player = Hand()
    dealer = Hand()
    player.add_card(deck.deal_card())
    player.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())

    if in_play:
        outcome = "You restarted the game"
        score -= 1
    else:
        outcome = "New game!"

    in_play = True


    #print "Player hand", str(player.get_value())
    #print "Dealer hand", str(dealer.get_value())

def hit():
    global score, in_play, outcome

    if in_play:
        player.add_card(deck.deal_card())
        #print "Player",str(player.get_value()),"Dealer",str(dealer.get_value())

        if player.get_value() > 21:
            outcome = "You have busted"
            in_play = False
            score -= 1
            #print outcome
            #outcome = "Dealer: " + str(dealer.get_value()) + "  Player: " + str(player.get_value())
            #print outcome

def stand():
    global score,outcome,in_play

    if in_play == False:
        outcome = "Game is over. Deal again!"
        #print outcome

    else:
        while dealer.get_value()<17:
            dealer.add_card(deck.deal_card())
            #print "Player",str(player.get_value()),"Dealer",str(dealer.get_value())

        if dealer.get_value()>21:
            outcome = "Dealer have busted. Deal again?"
            #print outcome
            score += 1
            in_play = False
            #print "Player",str(player.get_value()),"Dealer",str(dealer.get_value())

        elif dealer.get_value() > player.get_value():
            outcome = "Dealer wins. Deal again?"
            #print outcome
            score -= 1
            in_play = False
            #print "Player",str(player.get_value()),"Dealer",str(dealer.get_value())

        elif dealer.get_value() == player.get_value():
            outcome = "Tie game. Dealer wins. Deal again?"
            #print outcome
            score -= 1
            in_play = False

        elif dealer.get_value() < player.get_value():
            outcome = "You win. Deal again"
            #print outcome
            score += 1
            in_play = False
            #print "Player",str(player.get_value()),"Dealer",str(dealer.get_value())

def exit_game():
    frame.stop()

# draw handler
def draw(canvas):
    canvas.draw_text("Blackjack", [220,50], 48, "Yellow")
    canvas.draw_text("Score : " + str(score), [80,520], 36, "Black")
    canvas.draw_text("Dealer :", [80,110], 30, "Black")
    canvas.draw_text("Player :", [80,300], 30, "Black")
    canvas.draw_text(outcome, [80,560], 28, "White")
    dealer.draw(canvas, [80,135])
    player.draw(canvas, [80,325])

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.add_button("Exit", exit_game,200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric
