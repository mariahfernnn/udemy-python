# EXERCISE: Unlucky Numbers

# Loop through numbers 1-20 inclusive
# for 4 and 13, print "x is unlucky"
# for even numbers, print "x is even"
# for odd numbers, print "x is odd"

# for x in range(1,21):
# 	if x == 4 or x == 13:
# 		print(f"{x} is UNLUCKY!")
# 	elif x % 2 == 0:
# 		print(f"{x} is even")
# 	else:
# 		print(f"{x} is odd")

# refactoring - have one print statement at the end

for x in range(1,21):
	if x == 4 or x == 13:
		state = "unlucky"
	elif x % 2 == 0:
		state = "even"
	else:
		state = "odd"
	print(f"{x} is {state}")