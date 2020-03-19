# For loops in Python - More Exercise

print("How many times did you walk Yoyo today?")
walks = input()
# convert str to int
walks = int(walks)

for walk in range(walks):
	print(f"I walked Yoyo {walks} times today")