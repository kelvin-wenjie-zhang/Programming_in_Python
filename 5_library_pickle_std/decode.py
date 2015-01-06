# part2 (c)
from gen_key import Key
import sys
import pickle

def decode(encoded_message, key):
  # store the letter list
  letters = []
  # in order to decode the encrypted message,
  # we need to switch the key-value pair in the key dicrectory
  switch_key = {y:x for x,y in key.items()}

  # for each element in the list, the length is the value.
  # we find the respective key from the new dicrectory
  for item in encoded_message:
    value = len(item)
    key = switch_key[value]
    letters.append(key)

  # transform the list into a string type
  output = ""
  for item in letters:
    output += str(item)

  return output

def main():
  # command line arguments
  if len(sys.argv) < 3:
    print("Please provide a encoded file (argv[1]) and a Key object (argv[2]) on the command line.")
    sys.exit(0)

  else:
    # unpickle the encrypted message
    with open(sys.argv[1], 'rb') as f:
      encrypted = pickle.load(f)

    # if the message object is not a list at all,
    # we handle the Type Error by printing an error message
    # and terminate gracefully
    if not isinstance(encrypted, list):
      sys.stderr.write("Expected a message object that is a list.\n")
      # raise TypeError
      sys.stderr.write("TypeError has been raised.\n")
      sys.exit(0)

    # if the outer list contains a non-list element,
    # or there are too many elements in one of the inner lists.
    # we handle the TypeError by just skipping it.
    for item in encrypted:
      if not isinstance(item, list):
        encrypted.remove(item)
      elif len(item) > 26:
        encrypted.remove(item)

    # unpickle the cipher / key
    with open(sys.argv[2], 'rb') as f:
      cipher = pickle.load(f)

    # decode the encrypted message and print to the console
    print(decode(encrypted, cipher))


if __name__ == "__main__":
  main()
