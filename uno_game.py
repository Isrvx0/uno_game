from unoFunction import *


PLAY_AGAIN = True

print_blue     ("\n          WELCOME TO THE UNO-GAME        \n")
while HELP_CHOICE :
    start_screen        = title_screen()
    title_screen_option = start_screen_choice(start_screen)
    if start_screen != 'help':
        HELP_CHOICE = False
playersNumber = players_number()
playerNames   = players_name(playersNumber)

round_number = 1

while PLAY_AGAIN:
    player_turn = 0
    discards = []
    points_list = []
    NEW_ROUND = True

    pointList     = point_list(playerNames)
    unoDeck       = buildDeck()
    shuffle_deck(unoDeck)
    discards.append(unoDeck.pop(0)) 

    players_cards = dealCards(playersNumber , unoDeck)
    cardVal   = current_value (discards[-1])
    cardColor = current_color (discards[-1])
    discards = discards + unoDeck[::-3]
    
    while NEW_ROUND: 
        if check_unoDeck(unoDeck):
            shuffel_disc = shuffle_deck(discards)
            unoDeck = append_card(shuffel_disc , unoDeck)
            discards.clear()

        draw_card = False
        show_playerHand(playerNames[player_turn],players_cards[player_turn])
        
        if discards[-1] in WILD:
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
            elif cardVal == "Skip":
                player_turn = check_playerTurn(player_turn,playersNumber,PLAY_DIRECTION)
            if cardVal == "Draw Two" or discards[-1] == WILD[1] or cardVal == "Reverse":
                draw_card = True          
            
        else:
            print_red(CANT_PLAY)
            append_card(drawCard(1,unoDeck),players_cards[player_turn])
        
        if len(players_cards[player_turn]) == 1:
            print_red("\nBE CAREFULL! {} said UNO!".format(playerNames[player_turn]))
        
        player_turn = check_playerTurn(player_turn,playersNumber,PLAY_DIRECTION)
        
        if draw_card:
            if cardVal == "Draw Two":
                append_card(drawCard(DRAW_TWO_AMOUNT,unoDeck),players_cards[player_turn])
            if discards[-1] == WILD[1]:        
                append_card(drawCard(WILD_DRAW_FOUR_AMOUNT,unoDeck),players_cards[player_turn])

            if cardVal == "Reverse":
                playerNames.reverse()
                players_cards.reverse()
            draw_card = False

        if len(players_cards[player_turn-1]) <= 0:
            points = point_calculator(players_cards)
            pointList[playerNames[player_turn-1]] += points
            print(pointList)
            round_number += 1
            new_round(round_number,players_cards, playerNames, player_turn)
            NEW_ROUND = False
            
        if check_winner(pointList) != " ":
            winner_message(check_winner(pointList))
            PLAY_AGAIN = False