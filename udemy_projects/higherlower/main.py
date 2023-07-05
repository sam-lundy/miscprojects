import random
import os
from art import logo, vs
from game_data import data


def celeb_generator():
	random_celebrity = random.choice(data)
	return random_celebrity
	

def check_result(guess, first_follower_count, second_follower_count):
	if first_follower_count > second_follower_count:
		return guess == "a"
	else:
		return guess == "b"
	


def game():

	print(logo)
	score = 0
	should_continue = True
	first_celeb = celeb_generator()
	second_celeb = celeb_generator()

	while should_continue:
		first_celeb = second_celeb
		second_celeb = celeb_generator()

		while first_celeb == second_celeb:
			second_celeb = celeb_generator
	
		print(f"Compare A: {first_celeb['name']}, a {first_celeb['description']}, from {first_celeb['country']}.")

		if second_celeb["name"] == first_celeb["name"]:
			second_celeb = celeb_generator()

		print(vs)
		print(f"Against B: {second_celeb['name']}, a {second_celeb['description']}, from {second_celeb['country']}")

		guess = input("Who has more followers? Type 'A' or 'B': ").lower()
		first_follower_count = first_celeb["follower_count"]
		second_follower_count = second_celeb["follower_count"]

		is_correct = check_result(guess, first_follower_count, second_follower_count)

		os.system("clear")
		print(logo)

		if is_correct:
			score += 1
			print(f"You're right! Current score: {score}")
		else:
			should_continue = False
			print(f"Sorry, that's wrong. Final score: {score}")


game()
