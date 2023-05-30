COLORS = ["red","blue","yellow","green"]
VALUES =  list(range(0,10)) + ["Draw Two","Skip","Reverse"]
WILD   = ["Wild Card" , "Wild Draw Four"]    

ACTION_CARDS = ["Wild Card" , "Wild Draw Four" , "Draw Two","Skip","Reverse"]

YES_CHOICE = ['YES','yes','JA','ja']
NO_CHOICE = ['NO','no','NEE','nee']
START_SCREEN_OPTIONS = ['play','help','quit']

STARTING_HAND_SIZE = 7
DRAW_TWO_AMOUNT = 2
WILD_DRAW_FOUT_AMOUNT = 4


WINNER_POINTS = 500

ANIMATION = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
# animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]

PLAY_AGAIN = True
HELP_CHOICE = True

IVALID_CARD = "NOT a valid card. Please choose a valid card\n"
CANT_PLAY = "You CAN'T play. You need to draw a card"

INSTRUCTION = """
        > Each player draws a card, and the player with the highest card value start the game.
        > Each player will have 7 random cards.
        > The top card of the draw pile will be revealed and the game will start.
        > Play a card that matches the color, number, or symbol on the card.
        > Draw a card from the draw pile if you can't play a card.
        > Pay attention to action and Wild cards.
        > Write "Uno" if you only have 1 card left.
        > Play your last card to win the hand.
        > The points in each player's hand will be revealed at the end of each round.

    """