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
outcome = "New Game Starts!"
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
        self.cards = []

    def __str__(self):
        hand = "Hand Contains :"
        for card in self.cards:
            hand += " " + str(card)
        return hand    
            
    def add_card(self, card):
        self.cards.append(card)
        

    def get_value(self):
        value, num_ace = 0, 0
        for card in self.cards:
            value += VALUES[card.get_rank()]
            if(card.get_rank() == 'A'):
                num_ace += 1
            if(num_ace > 0 and value + 10 <= 21):
                value += 10
        return value
   
    def draw(self, canvas, pos):
        tmppos = pos[:]  
        for card in self.cards:  
            card.draw(canvas,tmppos)  
            tmppos[0]+=100   
        
# define deck class 
class Deck:
    def __init__(self):
        self.cards_deck = []
        for suit in SUITS:
            for rank in RANKS:
                card = Card(suit, rank)
                self.cards_deck.append(card)

    def shuffle(self):
        random.shuffle(self.cards_deck)

    def deal_card(self):
        return self.cards_deck.pop()
    
    def __str__(self):
        cards = "Deck Contains : "
        for card in self.cards_deck:
            cards += ' ' + str(card)
        return cards
        
#define event handlers for buttons
def deck_shuffle():
    global deck
    deck.shuffle()

def deal():
    global outcome, in_play, player, dealer, deck, in_play, score
    
    in_play = False
    deck = Deck()
    deck.shuffle()
    
    player, dealer = Hand(), Hand()
    player.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())   
    
    if in_play == True:
        outcome = "You Loose, New Game Starts!"
        score -= 1
    else:
        outcome = "New Game!"
    in_play = True

def hit():
    global in_play, player, outcome, deck, score
    
    if in_play:
        player.add_card(deck.deal_card())
        if (player.get_value() > 21):
            outcome = "You have busted!", player.get_value() , " > 21"
            score -= 1
            in_play = False
    
    
def stand():
    global in_play, player, dealer, outcome, deck, score
    
    if in_play and (player.get_value() > 21):
        outcome = "You have busted!",  player.get_value() , " > 21"
        score -= 1
    else:
        while(dealer.get_value() < 17):
            dealer.add_card(deck.deal_card())
    if player.get_value() > 21:
        outcome = "Dealer have busted, You Won!" ,  dealer.get_value() , " > 21"
        score += 1
    elif dealer.get_value() >= player.get_value():
        outcome = "You Loose!", player.get_value(), " < ", dealer.get_value()
        score -= 1
    elif dealer.get_value() < player.get_value():
        outcome = "You Won!", player.get_value(), " > ", dealer.get_value() 
        score += 1
            

# draw handler    
def draw(canvas):
    canvas.draw_text(str(outcome) + str("  Score : "+ str(score)), (150, 150), 25, "Black")
    
    pos=[100,300]  
    dealer.draw(canvas, pos)  
    player.draw(canvas, [pos[0],pos[1]+100])  


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Shuffle Deck", deck_shuffle, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric