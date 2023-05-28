import time 
import sys
from termcolor import colored

# making the deck :
def buildDeck():
    deck = []
    colors = ["red","blue","yellow","green"]
    values = [0,1,2,3,4,5,6,7,8,9,"Draw Two","Skip","Reverse"]
    wild   = ["Wild Card" , "Wild Draw Four"]    
    for color in colors:
         for value in values:
              card = "{} {}".format(color , value)
              deck.append(card)
              if value != 0: # -> because only one 0 card per color.
                   deck.append(card)
    for i in range (4):
         deck.append(wild[0])
         deck.append(wild[1])
    return deck

    
# title screen :
def title_screen():
    print_green    ("                 > Play                    \n")
    print_yellow   ("                 > Help                    \n")
    print_red      ("                 > Quit                  \n")
    choice = input (">  ")
    return choice.lower()

# options title screen :
def titleScreen_choice(option):
    if option == "play":
        print_magenta ("You have chosen the 'PLAY' option.\n")
        loading()
    elif option == "help":
        print_magenta ("You have chosen the 'HELP' option.\n")
    elif option == "quit":
        print_magenta ("You have chosen the 'QUIT' option.\nYou can always come back to play.")
        exit()


# Help option :
def help_option():
    print_red ("How to Play the Uno Game:\n")
    print_magenta ("""
        > Each player draws a card, and the player with the highest card value start the game.
        > Each player will have 7 random cards.
        > The top card of the draw pile will be revealed and the game will start.
        > Play a card that matches the color, number, or symbol on the card.
        > Draw a card from the draw pile if you can't play a card.
        > Pay attention to action and Wild cards.
        > Write "Uno" if you only have 1 card left.
        > Play your last card to win the hand.
        > The points in each player's hand will be revealed at the end of each round.

            Please select an option to continue.                  
    """)
    


# loading function :
def loading():
    time.sleep(0.1)
    # animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
    animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

    for i in range(20):
        time.sleep(0.1)
        sys.stdout.write("\rLOADING.... " + animation[i % len(animation)])
        sys.stdout.flush() 
    print_yellow("\nThe game will start in a few seconds!")
     
# slow print = 
def slowprint(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)

# colored text =
def print_colorvars(txt:str='{}', vars:list=[], color:str='yellow') -> None:
    vars = map(lambda string, color=color: colored(str(string), color, attrs=['bold']) ,vars)
    slowprint(txt.format(*vars))

def print_green(name:str) -> None:
    print_colorvars(vars=['{}'.format(name)], color='green')

def print_yellow(name:str) -> None:
    print_colorvars(vars=['{}'.format(name)], color='yellow')

def print_red(name:str) -> None:
    print_colorvars(vars=['{}'.format(name)], color='red')

def print_blue(name:str) -> None:
    print_colorvars(vars=['{}'.format(name)], color='blue')


def print_magenta(name:str) -> None:
    nextStep(1)
    print_colorvars(vars=['{}'.format(name)], color='magenta')

def nextStep(secwait:int=1) -> None:
    print('')
    time.sleep(secwait)








