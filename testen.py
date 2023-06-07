from uno_data import *
from unoFunction import * 

unoDeck = ["1","2","3"]
discard = ["1","1","1","1","1","1","1","1"]

if check_unoDeck(unoDeck):
        shuffel_disc = shuffle_deck(discard)
        unoDeck = append_card(shuffel_disc , unoDeck)
        discard.clear()

print(unoDeck)
print(discard)















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