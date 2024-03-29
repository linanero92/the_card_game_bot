# 1. Greeting
# 2. Game rules
# 3. Generating a random card
# 4. The question: name the color and suit of the card??
# 5. Game player response
# 6. Comparison of response
# 7.1 If the answer is correct, print "Correct!..."
# 7.2 If the answer is wrong, print "Incorrect!..."

print("Welcome to the game, dear user!")

print("I will generate a random card. You should guess the card's suit color")

print("Please, choose the game level?\n")

card_number = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
card_suit = ["H", "D", "S", "C"]
card_color = ["Red", "Black"]


from random import choice

random_card_number = choice(card_number)
random_card_suit = choice(card_suit)
random_card_color = choice(card_color)

level = int(input())

if level == 1:
    player_answer = input("Guess the color, Red or Black?\n")
    if player_answer == "Red" and random_card_color == "Red":
        print("Correct! The card was: " + random_card_number + random_card_suit)
    elif player_answer == "Black" and random_card_color == "Black":
        print("Correct! The card was: " + random_card_number + random_card_suit)
    else:
        print("Incorrect! The card was: " + random_card_color)

if level == 2:
    player_answer = input("Guess the number of the card?\n")
    if player_answer == "2" and card_number == "2":
        print("Correct! The card was: " + random_card_number)
    if player_answer == "3" and card_number == "3":
        print("Correct! The card was: " + random_card_number)
    if player_answer == "4" and card_number == "4":
        print("Correct! The card was: " + random_card_number)
    if player_answer == "5" and card_number == "5":
        print("Correct! The card was: " + random_card_number)
    if player_answer == "6" and card_number == "6":
        print("Correct! The card was: " + random_card_number)
    if player_answer == "7" and card_number == "7":
        print("Correct! The card was: " + random_card_number)
    if player_answer == "8" and card_number == "8":
        print("Correct! The card was: " + random_card_number)
    if player_answer == "9" and card_number == "9":
        print("Correct! The card was: " + random_card_number)
    if player_answer == "10" and card_number == "10":
        print("Correct! The card was: " + random_card_number)
    if player_answer == "J" and card_number == "J":
        print("Correct! The card was: " + random_card_number)
    if player_answer == "Q" and card_number == "Q":
        print("Correct! The card was: " + random_card_number)
    if player_answer == "K" and card_number == "K":
        print("Correct! The card was: " + random_card_number)
    if player_answer == "A" and card_number == "A":
        print("Correct! The card was: " + random_card_number)

if level == 3:
    player_answer = input("Guess the number and suit of the card?\n")
    if player_answer == "2H" and random_card_suit == "H" and card_number == "2":
        print("Correct! The card was: " + random_card_number + random_card_suit)
    elif player_answer == "3H" and random_card_suit == "H" and card_number == "3":
        print("Correct! The card was: " + random_card_number + random_card_suit)
    elif player_answer == "4H" and random_card_suit == "H" and card_number == "4":
        print("Correct! The card was: " + random_card_number + random_card_suit)
    elif player_answer == "5H" and random_card_suit == "H" and card_number == "5":
        print("Correct! The card was: " + random_card_number + random_card_suit)
    elif player_answer == "6H" and random_card_suit == "H" and card_number == "6":
        print("Correct! The card was: " + random_card_number + random_card_suit)
    elif player_answer == "7H" and random_card_suit == "H" and card_number == "7":
        print("Correct! The card was: " + random_card_number + random_card_suit)
    elif player_answer == "8H" and random_card_suit == "H" and card_number == "8":
        print("Correct! The card was: " + random_card_number + random_card_suit)
    elif player_answer == "9H" and random_card_suit == "H" and card_number == "9":
        print("Correct! The card was: " + random_card_number + random_card_suit)
    elif player_answer == "10H" and random_card_suit == "H" and card_number == "10":
        print("Correct! The card was: " + random_card_number + random_card_suit)
    elif player_answer == "JH" and random_card_suit == "H" and card_number == "J":
        print("Correct! The card was: " + random_card_number + random_card_suit)
    elif player_answer == "QH" and random_card_suit == "H" and card_number == "Q":
        print("Correct! The card was: " + random_card_number + random_card_suit)
    elif player_answer == "KH" and random_card_suit == "H" and card_number == "K":
        print("Correct! The card was: " + random_card_number + random_card_suit)
    elif player_answer == "AH" and random_card_suit == "H" and card_number == "A":
        print("Correct! The card was: " + random_card_number + random_card_suit)
    elif player_answer == "2D" and random_card_suit == "D" and card_number == "2":
        print("Correct! The card was: " + random_card_number + random_card_suit)
    elif player_answer == "3D" and random_card_suit == "D" and card_number == "3":
        print("Correct! The card was: " + random_card_number + random_card_suit)
    elif player_answer == "4D" and random_card_suit == "D" and card_number == "4":
        print("Correct! The card was: " + random_card_number + random_card_suit)
    elif player_answer == "5D" and random_card_suit == "D" and card_number == "5":
        print("Correct! The card was: " + random_card_number + random_card_suit)
    elif player_answer == "6D" and random_card_suit == "D" and card_number == "6":
        print("Correct! The card was: " + random_card_number + random_card_suit)
    elif player_answer == "7D" and random_card_suit == "D" and card_number == "7":
        print("Correct! The card was: " + random_card_number + random_card_suit)
    elif player_answer == "8D" and random_card_suit == "D" and card_number == "8":
        print("Correct! The card was: " + random_card_number + random_card_suit)
    elif player_answer == "9D" and random_card_suit == "D" and card_number == "9":
        print("Correct! The car Dwas: " + random_card_number + random_card_suit)
    elif player_answer == "10D" and random_card_suit == "D" and card_number == "10":
        print("Correct! The card was: " + random_card_number + random_card_suit)
    elif player_answer == "JD" and random_card_suit == "D" and card_number == "J":
        print("Correct! The card was: " + random_card_number + random_card_suit)
    elif player_answer == "QD" and random_card_suit == "D" and card_number == "Q":
        print("Correct! The card was: " + random_card_number + random_card_suit)
    elif player_answer == "KD" and random_card_suit == "D" and card_number == "K":
        print("Correct! The card was: " + random_card_number + random_card_suit)
    elif player_answer == "AD" and random_card_suit == "D" and card_number == "A":
        print("Correct! The card was: " + random_card_number + random_card_suit)
    elif player_answer == "2S" and random_card_suit == "S" and card_number == "2":
        print("Correct! The card was: " + random_card_number + random_card_suit)
    elif player_answer == "3S" and random_card_suit == "S" and card_number == "3":
        print("Correct! The card was: " + random_card_number + random_card_suit)
    elif player_answer == "4S" and random_card_suit == "S" and card_number == "4":
        print("Correct! The card was: " + random_card_number + random_card_suit)
    elif player_answer == "5S" and random_card_suit == "S" and card_number == "5":
        print("Correct! The card was: " + random_card_number + random_card_suit)
    elif player_answer == "6S" and random_card_suit == "S" and card_number == "6":
        print("Correct! The card was: " + random_card_number + random_card_suit)
    elif player_answer == "7S" and random_card_suit == "S" and card_number == "7":
        print("Correct! The card was: " + random_card_number + random_card_suit)
    elif player_answer == "8S" and random_card_suit == "S" and card_number == "8":
        print("Correct! The card was: " + random_card_number + random_card_suit)
    elif player_answer == "9S" and random_card_suit == "S" and card_number == "9":
        print("Correct! The card was: " + random_card_number + random_card_suit)
    elif player_answer == "10S" and random_card_suit == "S" and card_number == "10":
        print("Correct! The card was: " + random_card_number + random_card_suit)
    elif player_answer == "JS" and random_card_suit == "S" and card_number == "J":
        print("Correct! The card was: " + random_card_number + random_card_suit)
    elif player_answer == "QS" and random_card_suit == "S" and card_number == "Q":
        print("Correct! The card was: " + random_card_number + random_card_suit)
    elif player_answer == "KS" and random_card_suit == "S" and card_number == "K":
        print("Correct! The card was: " + random_card_number + random_card_suit)
    elif player_answer == "AS" and random_card_suit == "S" and card_number == "A":
        print("Correct! The card was: " + random_card_number + random_card_suit)
    elif player_answer == "2C" and random_card_suit == "C" and card_number == "2":
        print("Correct! The card was: " + random_card_number + random_card_suit)
    elif player_answer == "3C" and random_card_suit == "C" and card_number == "3":
        print("Correct! The card was: " + random_card_number + random_card_suit)
    elif player_answer == "4C" and random_card_suit == "C" and card_number == "4":
        print("Correct! The card was: " + random_card_number + random_card_suit)
    elif player_answer == "5C" and random_card_suit == "C" and card_number == "5":
        print("Correct! The card was: " + random_card_number + random_card_suit)
    elif player_answer == "6C" and random_card_suit == "C" and card_number == "6":
        print("Correct! The card was: " + random_card_number + random_card_suit)
    elif player_answer == "7C" and random_card_suit == "C" and card_number == "7":
        print("Correct! The card was: " + random_card_number + random_card_suit)
    elif player_answer == "8C" and random_card_suit == "C" and card_number == "8":
        print("Correct! The card was: " + random_card_number + random_card_suit)
    elif player_answer == "9C" and random_card_suit == "C" and card_number == "9":
        print("Correct! The card was: " + random_card_number + random_card_suit)
    elif player_answer == "10C" and random_card_suit == "C" and card_number == "10":
        print("Correct! The card was: " + random_card_number + random_card_suit)
    elif player_answer == "JC" and random_card_suit == "C" and card_number == "J":
        print("Correct! The card was: " + random_card_number + random_card_suit)
    elif player_answer == "QC" and random_card_suit == "C" and card_number == "Q":
        print("Correct! The card was: " + random_card_number + random_card_suit)
    elif player_answer == "KC" and random_card_suit == "C" and card_number == "K":
        print("Correct! The card was: " + random_card_number + random_card_suit)
    elif player_answer == "AC" and random_card_suit == "C" and card_number == "A":
        print("Correct! The card was: " + random_card_number + random_card_suit)
#elif player_answer not in card_number[0:13] and card_suit[0:4]:
    #print("The card doesn't exist")
    else:
        print("Incorrect! The card was: " + random_card_number + random_card_suit)





