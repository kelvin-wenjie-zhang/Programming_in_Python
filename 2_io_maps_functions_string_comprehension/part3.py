# Part 3 (12 points) - Function, Files, and String Processing

# (a)write a function that, given a fiename, opens the file in the format described and 
# reads in the data
def map_zip_town(f = open('markets.tsv','r',encoding = "iso-8859-1")):
	
	"""
	This function read a file named markets.tsv and then return two directory.
	One of them maps zip code to the farmer market record, the other maps town 
	to the zip codes.
	"""

	# these are the local variables that we want to return
	# although declearation is not necessary, it's only for personal preference :)
	zip = {}
	town = {}
	content = []

	# read the first line of the text
	l = f.readline()
	# keep reading the file until l returns empty string
	while l:
		# we split the string by a tab, and then append it to the content list
		content.append(l.split('\t'))
		# reads the next line
		l = f.readline()
	# close the file
	f.close()

	for i in range(len(content)):
		# collect all the unique zip codes as the keys for the zip directory
		zip[content[i][4]] = []
		# collect all the unique town names as the keys for the town directory
		town[content[i][3]] = []

	# search each zip code
	for code in list(zip.keys()):
		# search all the records
		for j in range(len(content)):
			# if the zip code is the same as the record's zip code
			if code == content[j][4]:
				# append this record to the list of the zip directory
				zip[code].append(content[j])

	# search each town
	for city in list(town.keys()):
		# search all the records
		for k in range(len(content)):
			# if the city name is the same as the record's city name
			if city == content[k][3]:
				# append this zip code in this record to the list of the town directory
				town[city].append(content[k][4])

	return zip, town

# (b) write a function that, given the parameters state, name,
# address, town, zip, returns a formatted string.

def my_format(my_string):
	"""
	This function would format a string by requirement.
	"""
	# \n is a new line feed
	# 0[1] is market name, 0[2] is the address
	# 0[3] is the city name, 0[0] is the state
	# 0[4] is the zip code
	output = "{0[1]}\n{0[2]}\n{0[3]}, {0[0]} {0[4]}\n".format(my_string)

	return output


# (c) write a program that first reads in the data file once, 
# and then asks the user repeatedly to enter a zip code or a town name.
# and then print all the farmer markets for this town or zip code

# first, we need to get our data from the file
zip, town = map_zip_town()
# ask for an input
command = input("Please enter a zip code or a town name (case sensitive) (type \"quit\" to exit): ")
# if the input is not 'quit'
while command != 'quit':
	# if the name is a zip code, we search it in the zip directory
	if command in zip:
		for count in range(len(zip[command])):
			print(my_format(zip[command][count]))
	# if the name is a town name, we search it in the town directory
	elif command in town:
		for a in range(len(town[command])):
			my_zip = town[command][a]
			for b in range(len(zip[my_zip])):
				print(my_format(zip[my_zip][b]))
	# if we cannot find it in zip directory or town directory, output error
	else:
		print("Sorry, we can't find it in our records. Please Try another one.")
	# continue the while loop
	command = input("Please enter a zip code or a town name (case sensitive) (type \"quit\" to exit): ")






















