# Part 1 (16pt) - Functional Programming

# a. (4pt) Printing Nested Lists:
def print_nlist(nlist, indent = 0):
	
	"""Print a nested list nlist in a readable format"""

	# loop all the element of the nlist
	for member in nlist:
		# if the element is a list and it is the first list in the nested list,
		# first we increment the indent to prepare 
		# for the next element, and then
		# we recursively call the function itself
		if isinstance(member, list) and nlist.index(member) == 1:
			indent += 1
			print_nlist(member, indent)
		# if the element is a list, but it's after some previous list,
		# we call the function itself recursively
		# without incement the indent
		elif isinstance(member, list) and nlist.index(member) > 1:
			print_nlist(member, indent)
		# if the element is a integer or a number,
		# we print it to the console.
		else:
			print('\t'*indent + str(member))
			

# indent variable would keep track of the indentation
indent = 0

# the nlist variable
nlist = [1,[2,[3,[4,5]]],[6,[7,[8,[9]],10]]]

# call the print_nlist function to print
print_nlist(nlist)



# b. (4pt) Mapping Nested Lists:

def map_nlist(nlist, fun):
	
	"""
	Return a new nested list in which each element n that is not a list 
	has been replaced with the result of applying fun to n.
	"""

	# create a local variable to print
	new_list = nlist

	# loop over each element in the new_list
	for element in new_list:
		# if the element is a list, 
		# call the function itself recursively
		if isinstance(element, list):
			map_nlist(element, fun)
		# otherwise, we apply the function to the element
		else:
			new_list[new_list.index(element)] = fun(element)

	# return the result
	return new_list

nlist = [1,[2,[3,[4,5]]],[6,[7,[8,[9]],10]]]
# call the function to test
print(map_nlist(nlist, lambda x: x*2))



# c. (4pt) Combining nested lists:

def combine_nlist(nlist, init, combiner):

	"""
	In each recursion step combine_nlist keeps track of some current value,
	initialized to init. Then it updates the current value by applying
	combiner repeatedly to the current value and the result of processing
	the next element of nlist recursively.
	Finally it returns the current value.
	"""

	# assign the init to the current value
	current = init
	
	# loop over all the elements in the nlist
	for e in nlist:
		# if it's a list, then we call the function recursively
		if isinstance(e, list):
			current = combine_nlist(e, current, combiner)
		# otherwise, we update the current value by using the 
		# combiner
		else:
			current = combiner(current, e)

	# return the current value
	return current

nlist = [1,[2,[3,[4,5]]],[6,[7,[8,[9]],10]]]
print(combine_nlist(nlist, 0, lambda x,y: x+y))


# d. (4pt) Flattening nested lists:

def flatten_nlist(nlist, out = []):

	"""
	Produce a flattened representation of a nested list.
	"""

	# loop over all the items in the nested list
	for item in nlist:
		# if the item is a list,
		# we call the function itself recursively
		if isinstance(item, list):
			flatten_nlist(item, out)
		# otherwise, it's a number
		# we append to the output list
		else:
			out.append(item)
	return out

# test the function
print(flatten_nlist(nlist))
