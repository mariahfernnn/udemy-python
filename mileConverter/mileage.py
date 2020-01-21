print("How many kilometres did you cycle today?")
# input gives us a str
kms = input()
# convert str to float
miles = float(kms)/1.60934

# round(thing to round, how many decimal points)
# do the math first
miles = round(miles, 2)
print(f"That is equal to {miles} miles ")

# able to do it in-line too
# print(f"That is equal to {round(miles, 2} miles ")
