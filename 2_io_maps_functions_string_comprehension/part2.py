#Part 2 (4) - Dictionaries
fruit_to_color = {'banana':'yellow', \
					'blueberry':'blue', \
					'cherry':'red', \
					'lemon':'yellow', \
					'kiwi':'green',\
					'strawberry':'red', \
					'tomato':'red'}

#create a global variable directory to store the result
color_to_fruit = {}

# store all the unique color values as our keys in the new directory map
for color in list(fruit_to_color.values()):
	color_to_fruit[color] = []

# we search all the fruits in the fruit_to_color directory according to 
# each color in the new color_to_fruit directory
for fruit in list(fruit_to_color.keys()):
	# we search all the colors to find the correct spot
	for color in list(color_to_fruit.keys()):
		# if the fruit's color is the same as the color we want,
		# we put this fruit into the list that maps to this color
		if fruit_to_color[fruit] == color:
			# append this fruit's name into the list
			color_to_fruit[color].append(fruit)

# print it to the concole
print(color_to_fruit)
