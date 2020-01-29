# Rock, Paper, Scissors Game

# import module
import random

# Ask Player 1 for move
player_1 = input("Hey Player 1! Rock, Paper, Scissors?: ")

# Play against the computer using randint
num = random.randint(0, 2)
if num == 0:
	computer = 'rock'
elif num == 1:
	computer = 'paper'
else:
	computer = 'scissors'
print(f"computer plays {computer}" )

if player_1 == computer:
	print("It's a tie!")
elif player_1 == 'rock':
	if computer == 'scissors':
		print('player 1 wins')
	elif computer == 'paper':
		print('computer wins')
elif player_1 == 'paper':
	if computer == 'rock':
		print('player 1 wins')
	elif computer == 'scissors':
		print('computer wins')
elif player_1 == 'scissors':
	if computer == 'paper':
		print('player 1 wins')
	elif computer == 'rock':
		print('computer wins')
else:
	# Empty string or string does not match conditions
	# Does not print out if player 1 enters the right input but player 2 does not
	print("Something went wrong")

# Print a bunch of lines to prevent cheating
# print('No cheating!')
# print('No cheating!')
# print('No cheating!')
# print('No cheating!')
# print('No cheating!')
# print('No cheating!')
# print('No cheating!')
# print('No cheating!')
# print('No cheating!')
# print('No cheating!')
# print('No cheating!')
# print('No cheating!')
# print('No cheating!')
# print('No cheating!')
# print('No cheating!')
# print('No cheating!')
# print('No cheating!')

# Ask Player 2 for move
# player_2 = input("Hey Player 2! Rock, Paper, Scissors?: ")

# Another round of refactoring?
# else statement: Any situation where player 2 wins

# Refactored code
# if player_1 == player_2:
# 	# If both players enter the same move
# 	# Also works if both players do not enter anything
# 	print("It's a tie!")
# elif player_1 == 'rock':
# 	if player_2 == 'scissors':
# 		print('player 1 wins')
# 	elif player_2 == 'paper':
# 		print('player 2 wins')
# elif player_1 == 'paper':
# 	if player_2 == 'rock':
# 		print('player 1 wins')
# 	elif player_2 == 'scissors':
# 		print('player 2 wins')
# elif player_1 == 'scissors':
# 	if player_2 == 'paper':
# 		print('player 1 wins')
# 	elif player_2 == 'rock':
# 		print('player 2 wins')
# else:
# 	# Empty string or string does not match conditions
# 	# Does not print out if player 1 enters the right input but player 2 does not
# 	print("Something went wrong")

# # Conditional Logic
# if player_1 == 'rock' and player_2 == 'paper':
# 	print('player 2 wins')
# elif player_1 == 'rock' and player_2 == 'scissors':
# 	print('player 1 wins')
# elif player_1 == 'paper' and player_2 == 'rock':
# 	print('player 1 wins')
# elif player_1 == 'paper' and player_2 == 'scissors':
# 	print('player 2 wins')
# elif player_1 == 'scissors' and player_2 == 'rock':
# 	print('player 2 wins')
# elif player_1 == 'scissors' and player_2 == 'paper':
# 	print('player 1 wins')
# elif player_1 == player_2:
# 	print("It's a tie!")
# else:
# 	# Empty string or string does not match conditions
# 	print("Something went wrong")
