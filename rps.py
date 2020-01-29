# Rock, Paper, Scissors Game

# Ask Player 1 for move
player_1 = input("Hey Player 1! Rock, Paper, Scissors?: ")

# Print a bunch of lines to prevent cheating
print('No cheating!')
print('No cheating!')
print('No cheating!')
print('No cheating!')
print('No cheating!')
print('No cheating!')
print('No cheating!')
print('No cheating!')
print('No cheating!')
print('No cheating!')
print('No cheating!')
print('No cheating!')
print('No cheating!')
print('No cheating!')
print('No cheating!')
print('No cheating!')
print('No cheating!')

# Play against the computer using randint
import random
computer = random.choice(['rock', 'paper', 'scissors'])

if player_1 == computer:
	# If both players enter the same move
	# Also works if both players do not enter anything
	print("It's a tie!")
elif player_1 == 'rock':
	if computer == 'scissors':
		print('player 1 wins')
elif player_1 == 'paper':
	if computer == 'rock':
		print('player 1 wins')
elif player_1 == 'scissors':
	if computer == 'paper':
		print('player 1 wins')
else:
	print("computer wins")

# Ask Player 2 for move
# computer = input("Hey Player 2! Rock, Paper, Scissors?: ")

# Another round of refactoring?
# else statement: Any situation where player 2 wins

# Refactored code
# if player_1 == computer:
# 	# If both players enter the same move
# 	# Also works if both players do not enter anything
# 	print("It's a tie!")
# elif player_1 == 'rock':
# 	if computer == 'paper':
# 		print('player 2 wins')
# 	elif computer == 'scissors':
# 		print('player 1 wins')
# elif player_1 == 'paper':
# 	if computer == 'rock':
# 		print('player 1 wins')
# 	elif computer == 'scissors':
# 		print('player 2 wins')
# elif player_1 == 'scissors':
# 	if computer == 'rock':
# 		print('player 2 wins')
# 	elif computer == 'paper':
# 		print('player 1 wins')
# else:
# 	# Empty string or string does not match conditions
# 	# Does not print out if player 1 enters the right input but player 2 does not
# 	print("Something went wrong")

# # Conditional Logic
# if player_1 == 'rock' and computer == 'paper':
# 	print('player 2 wins')
# elif player_1 == 'rock' and computer == 'scissors':
# 	print('player 1 wins')
# elif player_1 == 'paper' and computer == 'rock':
# 	print('player 1 wins')
# elif player_1 == 'paper' and computer == 'scissors':
# 	print('player 2 wins')
# elif player_1 == 'scissors' and computer == 'rock':
# 	print('player 2 wins')
# elif player_1 == 'scissors' and computer == 'paper':
# 	print('player 1 wins')
# elif player_1 == computer:
# 	print("It's a tie!")
# else:
# 	# Empty string or string does not match conditions
# 	print("Something went wrong")
