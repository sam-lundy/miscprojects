#Number Guessing Game Objectives:
import random
from numberguess_art import logo

EASY_TURNS = 10
HARD_TURNS = 5

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level.lower() == "easy":
        return EASY_TURNS
    else:
        return HARD_TURNS

def check_answer(guess, answer, turns):
    """checks answer against guesses, returns the number of turns remaining"""
    if guess == answer:
        print(f"Holy shit! You guessed {answer}, You win! ")
    elif guess < answer:
        print(f"Too low. Guess again: ")
        return turns - 1
    elif guess > answer:
        print(f"Too high. Guess again: ")
        return turns - 1


def guessnumber():

    print(logo)
    print("Welcome to the number guessing game! ")
    print("I'm thinking of a number between 1 and 100... ")
    answer = random.randint(1, 100)
    print(f"Pssst.. The correct answer is {answer}. ")

    turns = set_difficulty()
    guess = 0

    while guess != answer:
        print(f"You have {turns} turns remaining to guess the number. ")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose. ")
            return

guessnumber()