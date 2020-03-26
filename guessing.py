# Section 11: Guessing Game 

import random

random_number = random.randint(1,10) # numbers 1 - 10 (inclusive)

guess = input("Guess a number between 1 and 10: ")
guess = int(guess)

while guess != random_number:
	if guess > random_number:
		# print("TOO HIGH")
		guess = int(input("TOO HIGH... Guess again: "))
	elif guess < random_number:
		# print("TOO LOW")
		guess = int(input("TOO LOW... Guess again: "))
	# else:
	# 	guess = int(input("BINGO!"))
		# print("BINGO!")

	print("BINGO! You are correct.")

# handle user guesses
#	if they guess CORRECT, tell them they won
#		otherwise tell them if they are TOO HIGH or TOO LOW

# BONUS - let player play again if they want

