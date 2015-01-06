###############################################
#
# Please fill in your solutions for part 2 to 4 
# below. 

##############################################################################
# Part 2
# For each line in the following interactive Python interpreter session, write
# a short justification for the output, clearly indicating which objects are
# in memory and which variables refer to them (ignore garbage collection for
# this exercise)
# Add your explanations as a new comment after each line. 

#>>> y,x = [1], [1]
# x is a list containing 1, y is another list containing 1

#>>> x is y
# to see if x and y point to the same object
#False

# Justification:
# x and y are NOT the names for the same object.
# x is a reference (pointer) to a list object in the memory, while
# y is a reference (pointer) to another list object in the memory. 
# Thus x and y do not point to the same list object, although the elements 
# of the list obejct are the same.
# Thus, x and y are NOT equal.

#>>> x = y
# y's memory location is copied to x
#x is y
# to see if x and y point to the same object
#True

# Justification:
# Since y is the memory location of its list, then now x is the same memory location
# as y after this assignment.
# Therefore, x and y points to the same list object now. And x and y are equal now.


#>>> y = y + x
# This is a string operation. Before this y = y + x assignment, x and y are 
# the same string due to the previous x = y assignment.
# For convience, we denote the original length of x (or y) as l. --> length(x) = l
# Now after y = y + x assignment, length(y) = 2l.
#>>> x.append(y)
# Add the y string to the end of x. 
# Since x is of length l and y is of length 2l, then
# now x is a string of length 3l. --> length(x) = 3l
#>>> x == y
# to see if x and y are the same string
#False
# Since the length of x and y are different, they are definitely NOT equal to each other.

##############################################################################
# Part 3 - Lists and for-Loops
#
# Use two nested for loops to compute the value 
# of expressions of the form 
# (a[1]+...+a[m])*(b[1]+...+b[m]).
# 
# Assume that a and b are arbitrary sequences of numbers.
# For instance, for a = [1, 2, 4] and b = [2, 3] the result would be 35.

a = [1, 2, 4]
b = [2, 3]
#Your code starts here

#to store the result
result = 0

#to iterate each element in the 'a' list
for x in a:
	#to iterate each element in the 'b' list
	for y in b:
		#each element in 'a' should multiply by each element in 'b'
		# and then we sum them up to get the final result
		result = result + x * y

#print out the result to the concole
print('The part 2 result is: ' + str(result))

#Your code ends here


##############################################################################
# Part 4 - Loops, Strings, and Indices
#
# Given a string s create a second string s2 that is a copy of s but without 
# characters that have an identical element next to them.
#
# For instance the, string
# s = ’abbcaabcaa’
# should produce the answer ’acbc ’.
#
# Pay attention to the first and last element.
# 
# Instead of iterating over elements of s, you should iterate over
# indices of a (use range). This should work for arbitrary sequences of
# arbitary length. You can refer to a specific character in a string 
# using the index operation s[index]. The index of the first character is 0.
# In the above example s[0] equals ’a’ and s[3] equals ’c’.
s = 'abbcaabcaa'
#Your code starts here

#create an empty string to store the wanted string
s2 = ''

# We use a for loop for the characters between the start and the end of the string,
# and we consider the start and end character separately.

# First, we define the index to keep track of:
index = 0

# use a for loop to iterate the index of s string
for index in range(len(s)):

	# for the begining character, we only compare it to the next character.
	# if they are not the same, then we can append it to s2
	if index == 0 and s[index] != s[index + 1]:
		s2 = s2 + s[index]

	# for the last character, we only compare it to the previous character.
	# if they are not the same, then we can append it to s2
	elif index == (len(s) - 1) and s[index] != s[index - 1]:
		s2 = s2 + s[index]

	# for the rest of the characters, we need to compare the character to the
	# previous one and the next one.
	# if they are not the same, then we can append it to s2
	else:
		if s[index - 1] != s[index] and s[index] != s[index + 1]:
			s2 = s2 + s[index]

# print out the result to the concoles
print('The s2 string in part 3 is: ' + s2)

#Your code ends here
