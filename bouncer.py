# ask for age
age = input("How old are you: ")

# if age:
# 	# change str to int or code will not work
# 	age = int(age)
# 	if age >= 18 and age < 21:
# 		# 18-21 wristband
# 		print("You can enter, but need a wristband")
# 	elif age >= 21:
# 		# 21+ drink, normal entry
# 		print("You are good to enter and drink!")
# 	else:
# 		# too young, no entry
# 		print("You can't come in, little one!")
# else:
# 	print("Please enter an age!")

# refactored 
if age:
	# change str to int or code will not work
	age = int(age)
	if age >= 21:
		# check if over 21
		print("You are good to enter and drink!")
	elif age >= 18:
		# check if 18 but under 21
		print("You can enter, but need a wristband")
	else:
		print("You can't come in, little one!")
else:
	print("Please enter an age!")