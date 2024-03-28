# Greeting
# Game rools
# enerating a random card
# The question: red or black?
# Game player response
# Comparison of response
#


print('Welcome to the game, dear user!')

print("I will generate a random card. You should guess the card's suit color")


card_number = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '', '', 'J', 'Q', 'K', 'A']
card_suit = ['H', 'D', 'S', 'C']

from random import choice

random_card_number = choice(card_number)
random_card_suit = choice(card_suit)

player_answer = input("Guess the color of the card: Red or Black?\n")

if player_answer == "Red" and random_card_suitb == ["H", "D"]:
    print("Correct! The card was: " + random_card_number + random_card_suit)
elif player_answer == "Black" and random_card_suit in ["S", "C"]:
    print("Correct! The card was: " + random_card_number + random_card_suit)
else:
    print("Incorrect! The card was: " + random_card_number + random_card_suit)





