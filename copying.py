# EXERCISE: Stop Copying Me - While Loop

# Repeat user input until they say the magic word/phrase

copy = input("Are we there yet? ")

while copy != "I'll let you know when":
	print(copy)
	copy = input()
print("Yes, we're here!")