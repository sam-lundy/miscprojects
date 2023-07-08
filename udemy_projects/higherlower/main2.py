import random
import os
from art import logo, vs
from game_data import data


def get_random_account():
    return random.choice(data)


def format_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    followers = account["follower_count"]
    return f"{name}, a {description} from {country}"

def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

def game():
    print(logo)
    score = 0
    should_continue = True
    account_b = get_random_account()

    while should_continue:
        account_a = account_b
        account_b = get_random_account()

        while account_a == account_b:
            account_b = get_random_account()

        print(f"Compare A: {format_data(account_a)}.")
        print(vs)
        print(f"Against B: {format_data(account_b)}.")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        is_correct = check_answer(guess, account_a["follower_count"], account_b["follower_count"])

        os.system("clear")
        print(logo)

        if is_correct:
            score += 1
            print(f"Correct! Current score: {score}")
            
        else:
            print(f"Incorrect. Final score: {score}")
            should_continue = False

        
game()