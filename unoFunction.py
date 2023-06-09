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

# Draw card function :
def drawCard (numCards,unoDeck):
    cardsDraw = []
    for i in range (numCards):
        cardsDraw.append(unoDeck.pop(0))
    return cardsDraw

#check Uno Deck:
def check_unoDeck(unoDeck):
    if len(unoDeck) < 4:
        unoDeck = True
    else:
        unoDeck = False
    return unoDeck




# Deal cards to players: 
def dealCards (playersNumber , unoDeck):
    players_cards = [] # to store the players cards
    for x in range (playersNumber):
        cards = drawCard(STARTING_HAND_SIZE,unoDeck)
        players_cards.append(cards)
    return players_cards

# check if play_TURN == players_NUMBERS
def check_playerTurn(player_turn,players_number,playDirection):
    if player_turn >= players_number-1 :
        player_turn = 0  # ---> to start the round again
    elif player_turn < 0 :
        player_turn = players_number - 1   # ---> to start the round again
    else:
        player_turn += playDirection
    return player_turn

# show player cards function:
def show_playerHand (player , playerDic):
    print_yellow("\n{}'s turn\nPlease press enter to verify your id! ".format(player))
    input("\n")
    for i in range (len(playerDic)):
        print_magenta("Card {} = {}".format(i+1 , playerDic[i]))

# check if player can play:
def canPlay(cardVal, cardColor, playerHand):
    for card in playerHand:
        if "Wild" in card:
            return True
        elif cardVal in card or cardColor in card:
            return True
    return False

# Check played card :
def check_playedCard(cardVal, cardColor, players_cards):
    not_vaild_card = True
    while not_vaild_card :
        try:
            chosen_card = int(input(CARD_CHOICE))
            if not canPlay(cardVal, cardColor,[players_cards[chosen_card-1]]):
                print_red(IVALID_CARD)
            else:
                not_vaild_card = False
        except ValueError:
            print_red(IVALID_NUMBER)
    return chosen_card

# check if other player have "Draw 2" or "Draw 4" card:
# def drawCard_check (playerCard,CardVal):
#     for card in playerCard:
#         splited_card = card.split(" ", 1)
#         if splited_card[0] == CardVal:
#             drawCrad = "YES"
#         else:
#             drawCrad = "NO"
#     return drawCrad


# Points list = 
def point_list(players_name):
    point = {}
    for name in players_name:
        point[name] = 0
    return point

# Point calculator :
def point_calculator(players_hand):
    points = 0
    for cards in players_hand:
        for card in cards:
            splitCard = card.split(" ", 1)
            if card in WILD:
                points += 50
            elif splitCard[1] in POINTS_20:
                points += 20
            else:
                points += int(splitCard[1])
    return points

# Check winner :
def check_winner(players_points):
    for key , value in players_points.items():
        if value >= 500:
            winner = key
        else:
            winner = " " 
    return winner

# Winner's message :
def winner_message(winner_name):
    print_green("THE WINNER IS {}!".format(winner_name))
    print_blue(WINNER_DRAWING)
    print_yellow("\nYOU DID A GREAT JOB! .. SEE YOU NEXT TIME!")


# NEW ROUND :
def new_round(round_number,players_cards,playerNames,player_turn):
    print_magenta('Winner of this round = {}'.format(playerNames[player_turn-1]))
    print_blue("\nROUND = {}".format(round_number))
    

# append card to player hand while playing
def append_card(draw_cards , player_hands):
    for card in draw_cards:
            player_hands.append(card)
    return player_hands

# Current color :
def current_color(discard):
    splitCard = discard.split(" ", 1)
    return splitCard[0]

# Current value :
def current_value(discard):
    splitCard = discard.split(" ", 1)
    if splitCard[0] == "Wild":
        cardVal = "Any"
    else:
        cardVal = splitCard[1]
    return cardVal

# Wild card :
def wild_Card():
    forLoop_print(COLORS)
    valid_number = True
    while valid_number:
        try:
            color = int(input(COLOR_CHOICE))
            cardColor = COLORS[color-1] 
            valid_number = False
        except ValueError:
            print_red(IVALID_NUMBER)    
    return cardColor


# print in for loop:
def forLoop_print(list):
    i = 1
    for element in list:
        print_magenta("{}) {}".format(i , element))
        i += 1

# Ask the number of players :
def players_number():
    valid_answer = True
    while valid_answer:
        try:
            players = int(input("How many players? \n> "))
            if players < 2 or players > 4:
                print_red('Please enter a number between 2 and 4.\n')
            else:
                valid_answer = False
        except ValueError:
            print_red("Please enter a valid number.")
        
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
    while deck[0] in WILD:
        random.shuffle(deck)
    return deck

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
        print_magenta (PLAY_OPTION)
        loading()
    elif option == "quit":
        print_magenta (HELP_OPTION)
        exit()
    elif option == "help":
        print_magenta (HELP_OPTION)
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









