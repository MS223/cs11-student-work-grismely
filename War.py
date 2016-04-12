player_1 = raw_input("Player 1, what's your name?")
player_2 = raw_input("Player 2?")


import random

def shuffled_deck():
    deck = range(2,53)
    random.shuffle(deck)
    print deck

def player_turn(player_name):
    card = deck.pop()
    print player_name + " drew card, " + card
    print str(card)

deck = []
player_turn(player_1)
