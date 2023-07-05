from blackjack_art import logo
import random
import os

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, cpu_score):
    if user_score == cpu_score:
        return f"Scores are tied at {user_score}. It's a draw. "
    elif user_score == 0:
        return "Blackjack! You win!"
    elif cpu_score == 0:
        return "Computer has blackjack! You lose..."
    elif cpu_score > 21:
        return "Computer Bust! You win!"
    elif user_score > cpu_score:
        return "You win!"
    else:
        return "You lose.."

def blackjack():
    print(logo)
    user_cards = []
    cpu_cards = []
    user_score = 0
    cpu_score = 0
    is_game_over = False

    for i in range(2):
        user_cards.append(deal_card())
        cpu_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        cpu_score = calculate_score(cpu_cards)
        print(f"Your cards are {user_cards} with a total of {user_score}")
        print(f"Computer's first card: {cpu_cards[0]}")

        if user_score == 0 or cpu_score == 0 or user_score > 21:
            is_game_over = True
        else:
            hit_me = input(f"Would you like another card? 'y' or 'n': ")
            if hit_me.lower() == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while cpu_score != 0 and cpu_score < 17:
        cpu_cards.append(deal_card())
        cpu_score = calculate_score(cpu_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {cpu_cards}, final score: {cpu_score}")
    print(compare(user_score, cpu_score))

while input("Do you want to play Blackjack? Type 'y' or 'n': ") == "y":
    os.system("clear")
    blackjack()
