import time 
import sys
import random
from termcolor import colored
from uno_data import *

# making the deck :
def buildDeck():
    deck = []
    for color in COLORS:
         for value in VALUES:
              card = "{} {}".format(color , value)
              deck.append(card)
              if value != 0: # -> because only one 0 card per color.
                   deck.append(card)
    for i in range (4):
         deck.append(WILD[0])
         deck.append(WILD[1])
    return deck

# Ask the number of players :
def players_number():
    valid_answer = True
    while valid_answer:
        try:
            players = int(input("How many players? \n> "))
            if players < 2 or players > 4:
                print('Please enter a number between 2 and 4.\n')
            else:
                valid_answer = False
        except ValueError:
            print("Please enter a valid number.")
        
    return players

# Ask the name of players :
def players_name(playersNumber):
    number = 1
    names_list = []
    while number <= playersNumber:
        playerName = input(f"What is the name of player {number}? \n> ")
        if playerName in names_list:
            print('The name exists in the list\n')
        else:
            number += 1
            names_list.append(playerName)
    return names_list

# shuffle the deck :
def shuffle_deck (deck):
    for i in range (2):
        random.shuffle(deck)
    return deck

# Draw card function :
def drawCard (numCards,unoDeck):
    cardsDraw = []
    for i in range (numCards):
        cardsDraw.append(unoDeck.pop(0))
    return cardsDraw

# Deal cards to players: 
def dealCards (playersNumber , unoDeck):
    players_cards = [] # to store the players cards
    for x in range (playersNumber):
        cards = drawCard(7,unoDeck)
        players_cards.append(cards)
    return players_cards

# Check special card ::
def special_card(discards):
    played_color  = discards[0].split()
    if played_color == "wild":
        print(COLORS)
        color = int(input("What color would you like to chose? \n>  "))



# check if play_TURN == players_NUMBERS
def check_playerTurn(player_turn,players_number):
    if player_turn == players_number-1 :
        player_turn = 0  # ---> to start the round again
    elif player_turn < 0 :
        player_turn = players_number - 1   # ---> to start the round again
    else:
        player_turn += 1
    return player_turn

# append card to player hand while playing
def append_card(draw_cards , player_hands):
    for card in draw_cards:
            player_hands.append(card)
    return player_hands

# show player cards function:
def show_playerHand (player , playerDic):
    print_yellow("\n{}'s turn\nPlease press enter to verify your id! ".format(player))
    input("\n")
    for i in range (len(playerDic)):
        print_magenta(" card {} = {}".format(i+1 , playerDic[i]))

# check if player can play:
def canPlay(discards, playerHand):
    splited_card = discards.split(" ",1)

    for card in playerHand:
        if "Wild" in card:
            return True
        elif discards in card:
            return True
        elif splited_card[0] in card or splited_card[1] in card:
            return True
    return False

# check if player played the right card:
def chech_playedCard(discards,players_cards):
    not_vaild_card = True
    while not_vaild_card :
        try:
            chosen_card = int(input("Wich card do you want to play? \n> "))
            if not canPlay(discards,[players_cards[chosen_card-1]]):
                print_red(IVALID_CARD)
            else:
                not_vaild_card = False
        except ValueError:
            print_red("NOT a valid number. Please choose a valid number\n")
    return chosen_card

# title screen :
def title_screen():
    valid_answer = True
    while valid_answer:
        print_green    ("                 > Play                    \n")
        print_yellow   ("                 > Help                    \n")
        print_red      ("                 > Quit                  \n")
        choice = input (">  ")
        if choice.lower() not in START_SCREEN_OPTIONS:
            print_red("Please enter a valid answer\n")
        else:
            valid_answer = False
    return choice.lower()

# options title screen :
def start_screen_choice(option):
    if option == "play":
        print_magenta ("You have chosen the 'PLAY' option.\n")
        loading()
    elif option == "quit":
        print_magenta ("You have chosen the 'QUIT' option.\nYou can always come back to play.")
        exit()
    elif option == "help":
        print_magenta ("You have chosen the 'HELP' option.\n")
        help_option()


# Help option :
def help_option():
    explanation = True
    while explanation:
        print_red ("How to Play the Uno Game:\n")
        print_magenta (INSTRUCTION)
        extra_explanation = input("Was the explanation clear enough for you?\n>  ")
        
        if extra_explanation.lower() not in YES_CHOICE :
            print_blue("we're going to give the explanation one more time\n")
        else:
            print_magenta("Please select an option to continue.")
            explanation = False


# loading function :
def loading():
    time.sleep(0.1)
    for i in range(20):
        time.sleep(0.1)
        sys.stdout.write("\rLOADING.... " + ANIMATION[i % len(ANIMATION)])
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
    print(txt.format(*vars))

def print_green(name:str) -> None:
    print_colorvars(vars=['{}'.format(name)], color='green')

def print_yellow(name:str) -> None:
    print_colorvars(vars=['{}'.format(name)], color='yellow')

def print_red(name:str) -> None:
    print_colorvars(vars=['{}'.format(name)], color='red')

def print_blue(name:str) -> None:
    print_colorvars(vars=['{}'.format(name)], color='blue')


def print_magenta(name:str) -> None:
    print_colorvars(vars=['{}'.format(name)], color='magenta')

def nextStep(secwait:int=1) -> None:
    print('')
    time.sleep(secwait)








