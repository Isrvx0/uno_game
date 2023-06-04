COLORS = ["red","blue","yellow","green"]
VALUES =  list(range(0,10)) + ["Draw Two","Skip","Reverse"]
WILD   = ["Wild Card" , "Wild Draw Four"]    

POINTS_20 = ["Draw Two","Skip","Reverse"]


ACTION_CARDS = ["Wild Card" , "Wild Draw Four" , "Draw Two","Skip","Reverse"]

YES_CHOICE = ['YES','yes','JA','ja']
NO_CHOICE = ['NO','no','NEE','nee']
START_SCREEN_OPTIONS = ['play','help','quit']

STARTING_HAND_SIZE = 7
DRAW_TWO_AMOUNT = 2
WILD_DRAW_FOUR_AMOUNT = 4

player_turn = 0
play_direction = 1
round_number = 1

discards = []
points_list = []

WINNER_POINTS = 500

ANIMATION = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
# animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]

NEW_ROUND = True
HELP_CHOICE = True

IVALID_CARD = "NOT a valid card. Please choose a valid card\n"
CANT_PLAY = "You CAN'T play. You need to draw a card"
IVALID_NUMBER = "NOT a valid number. Please choose a valid number\n"

TOP_CARD = "Card on the top of discards pile: "
TOP_COLOR = "Color on the top of discards pile: "

CARD_CHOICE = "Wich card do you want to play? \n> "
COLOR_CHOICE = "What color would you like to chose? \n>  "


PLAY_OPTION = "You have chosen the 'PLAY' option.\n"
HELP_OPTION = "You have chosen the 'HELP' option.\n"
QUIT_OPTION = "You have chosen the 'QUIT' option.\nYou can always come back to play."


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


WINNER_DRAWING = """

                 @@  @@ 
                ,-@@~@-.   
 _              (_, O _/   
| Y~.            (__d._)    
| r.|    Y@oooood@@@@@@@@oooo@F 
 Y ||   _Y@@@@@@P   "V"  Y@@@@f 
 | t_\_/ _)@@@@@          @@@@f  __     ,--,
  \  `. / ~@@@@@    . .   @@@@  (_ `---'  ~~)
   `-._/)   @@@@b__|@_@|_d@@@    _l,'~   ~~)
      (,db   (   _  `-' _   )  ,d@_)---~~~~
         Yb.  \ '|\____/|` / od@P 
          Y@b  \ | nn  /','d@@P 
            Y@b `\`---'/'od@P 
             ~@@@@`---'@@@P~
               Y@@@@@@@@@~
                @@@@@@@@

"""