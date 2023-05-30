from unoFunction import *

player_turn = 0
play_direction = 1
discards = []

print_blue     ("\n          WELCOME TO THE UNO-GAME        \n")
while HELP_CHOICE :
    start_screen        = title_screen()
    title_screen_option = start_screen_choice(start_screen)
    if start_screen != 'help':
        HELP_CHOICE = False

playersNumber = players_number()
playerNames   = players_name(playersNumber)
unoDeck       = buildDeck()
shuffle_deck(unoDeck)
discards.append(unoDeck.pop(0)) # check if it's a wild or draw card 

players_cards = dealCards(playersNumber , unoDeck)

while PLAY_AGAIN:
    show_playerHand(playerNames[player_turn],players_cards[player_turn])
    print_blue("\nCard on the top of discards pile: {}".format(discards[-1]))

    if canPlay(discards[0], players_cards[player_turn]):
        chosen_card = chech_playedCard(discards[0],players_cards[player_turn])
        print_green("{} played with the card : {}".format(playerNames[player_turn],players_cards[player_turn][chosen_card-1]))
        discards.append(players_cards[player_turn].pop(chosen_card-1))
    else:
        print_red(CANT_PLAY)
        append_card(drawCard(1,unoDeck),players_cards[player_turn])
     
    
    player_turn = check_playerTurn(player_turn,playersNumber)
    