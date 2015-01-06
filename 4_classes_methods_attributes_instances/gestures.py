from random import randint
# Part 2 (10 points) - Overloading Special Methods

#(a) Define three classes Rock, Scissors, and Paper

class Rock(object):

	"""
	Rock class
	"""

	# overload the lt method
	def __lt__(self, other):
		if isinstance(other, Paper):
			return True
		elif isinstance(other, Rock):
			return False
		elif isinstance(other, Scissors):
			return False

	# overload the gt method
	def __gt__(self, other):
		if isinstance(other, Paper):
			return False
		elif isinstance(other, Rock):
			return False
		elif isinstance(other, Scissors):
			return True

	# overload the eq method
	def __eq__(self, other):
		if isinstance(other, Paper):
			return False
		elif isinstance(other, Rock):
			return True
		elif isinstance(other, Scissors):
			return False

	# overload the str method, so that we can print it
	def __str__(self):
		return "Rock"

class Paper(object):

	"""
	Paper class
	"""

	def __lt__(self, other):
		if isinstance(other, Paper):
			return False
		elif isinstance(other, Rock):
			return False
		elif isinstance(other, Scissors):
			return True

	def __gt__(self, other):
		if isinstance(other, Paper):
			return False
		elif isinstance(other, Rock):
			return True
		elif isinstance(other, Scissors):
			return False

	def __eq__(self, other):
		if isinstance(other, Paper):
			return True
		elif isinstance(other, Rock):
			return False
		elif isinstance(other, Scissors):
			return False

	def __str__(self):
		return "Paper"

class Scissors(object):

	"""
	Scissors class
	"""

	def __lt__(self, other):
		if isinstance(other, Paper):
			return False
		elif isinstance(other, Rock):
			return True
		elif isinstance(other, Scissors):
			return False

	def __gt__(self, other):
		if isinstance(other, Paper):
			return True
		elif isinstance(other, Rock):
			return False
		elif isinstance(other, Scissors):
			return False

	def __eq__(self, other):
		if isinstance(other, Paper):
			return False
		elif isinstance(other, Rock):
			return False
		elif isinstance(other, Scissors):
			return True

	def __str__(self):
		return "Scissors"


#(b) Create a class Player
class Player(object):

	"""
	A player class with a random choice of gesture
	"""

	def play(self):
		# choose a random number from 1 to 3
		i = randint(1,3)
		if i == 1:
			return Rock();
		elif i == 2:
			return Paper();
		elif i == 3:
			return Scissors();

#(c) Implement a class HumanPlayer
class HumanPlayer(Player):

	"""
	A human player class that overloads player class
	"""

	def play(self):
		# keep looping until we get the gesture
		while True:
			s = input("Please enter your gesture (Rock, Paper, Scissors): ")
			if s == "Rock":
				return Rock()
			elif s == "Paper":
				return Paper()
			elif s == "Scissors":
				return Scissors()
			# if the user type quit, 
			# return to the main function to end the loop
			elif s == "quit":
				return False
			# in case the user types invalid gesture
			else:
				print("Please enter a valid gesture.")


def main():
	
	"""
	The main funcion
	"""

	# how many times human wins
	win_human = 0
	# how many times human loses
	lost_human = 0
	# how many times computer wins
	win_computer = 0
	# how many times computer loses
	lost_computer = 0
	# draw games
	draw = 0

	while True:
		print("Type \"quit\" to quit.")
		
		# create an instance of gesture
		human = HumanPlayer().play()

		# check if the user want to quit
		if human == False:
			print("Good Bye")
			break
		else:
			computer = Player().play()
			# human wins
			if human > computer:
				win_human += 1
				lost_computer += 1
			# human lost
			elif human < computer:
				win_computer += 1
				lost_human += 1
			# draw game
			elif human == computer:
				draw += 1
			# print out the result
			print("Human: {0}\nComputer: {1}".format(str(human),str(computer)))
			print("Human Player: win {0}, lost {1}, draw games {2}".format(win_human, lost_human, draw))
			print("Computer Player: win {0}, lost {1}, draw games {2}".format(win_computer, lost_computer, draw))
			print("\n")


if __name__ == "__main__": # Default "main method" idiom.
    main()







