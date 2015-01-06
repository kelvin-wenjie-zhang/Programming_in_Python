# Part 2(4pt) - Generators
def ngrams(n, s):

	"""
	A generator function that takes a list of words and acts as 
	an iterator over all n-grams in this sentence.
	"""

	# we loop each word from i = 0 to len(s) - n + 1
	# so that we can have n-gram all the time
	for i in range(len(s)-n+1):
		# the generator is executed up to yield and interupted
		yield s[i:i+n]


s = "the quick red fox jumps over the lazy brown dog"
for x in ngrams(3, s.split()):
	print(x)