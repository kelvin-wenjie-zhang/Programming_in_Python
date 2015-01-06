# Part 2 (b)
from gen_key import Key
import sys
import pickle

# extend the value error exception
class EncodingException(ValueError):

  """
  An exception that will be raised if an input
  symbol cannot be encoded.
  """

def encode(message, key):
  # the return output
  output = []
  # loop over the letters
  for char in message:

    # if the character is between A to Z or it is a whitespce,
    # we can encode it
    if char == ' ' or (char <= 'Z' and char >= 'A'):
      # map the letter to numbers
      value = key[char]
      element = []
      while value > 0:
        # it doesn't have to be 1, it can be any object
        element.append(1)
        value -= 1
      output.append(element)
    # if the character is not ligit,
    # we raise an exception
    else:
      raise EncodingException
      return null

  return output

def main():
  if len(sys.argv) < 3:
    print("Please provide a Key object (argv[1]) and a file name (argv[2]) on the command line.")
    sys.exit(0)
  else:
    # write the cipher to a file
    with open(sys.argv[1],'rb') as f:
      cipher = pickle.load(f)

    # keep looping until a valid input is read
    while True:
      try:
        # encrypte the message by calling encode() function
        encrypted = encode(input("Please enter a message: ").upper(), cipher)
        break
      # catch an exception
      except EncodingException:
        print("Please enter upper case alphabets or whitespace only.")

    # write the encrypted message to a file
    with open(sys.argv[2],'wb') as f:
      pickle.dump(encrypted, f)

if __name__ == "__main__":
  main()
