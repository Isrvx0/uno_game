from unoFunction import *
playersNumber = players_number()
playerNames   = players_name(playersNumber)
unoDeck       = buildDeck()
shuffle_deck(unoDeck)
playerTurn = 0
players_cards = dealCards(playersNumber , unoDeck)
print(players_cards[playerTurn])
append_card(drawCard(1,unoDeck) , players_cards[playerTurn])

print(players_cards[playerTurn])




















    # print("The cards are:")
    # for (x,y) in zip(playerNames, players_cards):
    #     print("Player {} has {}".format(x, y))
    # print("")

    





# # check if player can play:
# def canPlay(color, value, playerHand):
#     for card in playerHand:
#         splitCard = card.split()
#         color = splitCard[0]
#         value = splitCard[1]