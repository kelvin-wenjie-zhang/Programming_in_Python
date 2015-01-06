# Part2 (8 points) - Object Serialization and Command Line Arguements
import string
import random
import pickle
import sys

# extends dictionary
class Key(dict):

  def __init__(self):
    # generate a list of letters
    letter_space = list(string.ascii_uppercase)
    # append a whitespace
    letter_space.append(' ')

    # generate a list of numbers
    number = list(range(27))
    # shuffle it
    random.shuffle(number)
    # matching letters and numbers
    mapping = list(zip(letter_space, number))

    # create the dictionary
    for item in mapping:
      self[item[0]] = item[1]

def main():
  if len(sys.argv) < 2:
    print("Please provide a file name on the command line.")
    sys.exit(0)
  else:
    file_name = sys.argv[1]
    # instantiate the key class
    cipher = Key()
    # write to a file
    with open(file_name,'wb') as f:
      pickle.dump(cipher, f)

if __name__ == "__main__":
  main()
