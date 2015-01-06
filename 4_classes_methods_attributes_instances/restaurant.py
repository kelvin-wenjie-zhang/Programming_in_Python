# Part1 (10 points) - Classes, Methods, Attributes, Instances

#(a) create a class Guest that represents a hungry guest at a restaurant
class Guest(object):

	"""
	A class that represents a hungry guest at a restaurant
	"""

	def __init__(self, name, hunger):
		# the guest attributes
		self.name = name
		self.hunger = hunger

	def eat(self):
		# if the guest is not hungry
		if self.hunger == 0:
			return "{0}: {1}".format(self.name, "Burp!")
		# if the guest is hungry, we decrement the hunger attribute
		else:
			self.hunger = self.hunger - 1
			return "{0}\n{1}: {2}".format("Yummy", "Hunger Value", self.hunger)


#(b) create a class Restaurant with base class list
class Restaurant(object):

	"""
	Restaurant class. Each element in a restaurant represents a table
	"""

	# restaurant base class
	table = []

	def __init__(self, size):
		# the restaurant attribute
		self.size = size
		self.table = []
		# initialize the table list
		while size > 0:
			self.table.append(None)
			size = size - 1

	def seat(self, guest):
		# if there's no None table, then it means there's no free table
		if self.table.count(None) == 0:
			print("No free table.")
			return False
		else:
			# remove the first None,
			# and replace it with the guest
			seat_no = self.table.index(None)
			self.table.remove(None)
			self.table.insert(seat_no, guest)

			# print the info of the guest and the table
			print("Seating guest {0} at table {1}.".format(self.table[seat_no].name, seat_no))
			return True

	def serve(self):
		# if all the guest in the table are None,
		# it means there's no guest
		if self.size == self.table.count(None):
			print("No guest to serve.")
			return None
		else: 
			# loop over all the guest
			for guest in self.table:
				# if it's None, continue the loop
				if guest is None:
					continue
				# if the guest is hungry, call the eat() method
				elif guest.hunger > 0:
					print("Serving guest {0}".format(guest.name))
					guest.eat()
					# if the guest become no hungry,
					# print the eat() method message,
					# and remove the guest from the table list
					if guest.hunger == 0:
						print(guest.eat())
						seat_no = self.table.index(guest)
						self.table.remove(guest)
						self.table.insert(seat_no, None)
					# we only serve only one guest at a time
					break
