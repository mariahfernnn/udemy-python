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

# Ask Player 2 for move
player_2 = input("Hey Player 2! Rock, Paper, Scissors?: ")

# Conditional Logic
if player_1 == 'rock' and player_2 == 'paper':
	print('player 2 wins')
elif player_1 == 'rock' and player_2 == 'scissors':
	print('player 1 wins')
elif player_1 == 'paper' and player_2 == 'rock':
	print('player 1 wins')
elif player_1 == 'paper' and player_2 == 'scissors':
	print('player 2 wins')
elif player_1 == 'scissors' and player_2 == 'rock':
	print('player 2 wins')
elif player_1 == 'scissors' and player_2 == 'paper':
	print('player 1 wins')
elif player_1 == player_2:
	print("It's a tie!")
else:
	print("Something went wrong")
