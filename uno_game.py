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
cardVal   = current_value (discards[-1])
cardColor = current_color (discards[-1])

while PLAY_AGAIN:
    draw_card = False
    show_playerHand(playerNames[player_turn],players_cards[player_turn])
    
    if len(cardColor)== 1:
        print_blue("\n{}{}".format(TOP_COLOR,cardColor))
    else:
        print_blue("\n{}{}".format(TOP_CARD,discards[-1]))

    if canPlay(cardVal, cardColor, players_cards[player_turn]):
        chosen_card = check_playedCard(cardVal, cardColor, players_cards[player_turn])
        print_green("{} played with the card : {}".format(playerNames[player_turn],players_cards[player_turn][chosen_card-1]))
        discards.append(players_cards[player_turn].pop(chosen_card-1))
        
        cardVal   = current_value (discards[-1])
        cardColor = current_color (discards[-1])
        
        if cardColor == "Wild" or cardColor == "Any":
            cardColor = wild_Card()
        elif cardVal == "Reverse":
            play_direction *= -1
        elif cardVal == "Skip":
            player_turn += 1
        if cardVal == "Draw Two" or discards[-1] == WILD[1]:
            draw_card = True          
        
    else:
        print_red(CANT_PLAY)
        append_card(drawCard(1,unoDeck),players_cards[player_turn])
    
    player_turn = check_playerTurn(player_turn,playersNumber,play_direction)
    
    if draw_card: 
        if cardVal == "Draw Two":
                append_card(drawCard(DRAW_TWO_AMOUNT,unoDeck),players_cards[player_turn])
        if discards[-1] == WILD[1]:
                append_card(drawCard(WILD_DRAW_FOUR_AMOUNT,unoDeck),players_cards[player_turn])

    if len(players_cards[player_turn]) <= 0:
        print(f'winner is {(players_cards[player_turn-1])}')
        PLAY_AGAIN = False