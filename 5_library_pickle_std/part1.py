#Part1 (6 points) - Searching the File System

# This script file will NOT search the entire computer unless you put
# it under the root directory.

# Please make sure the provided base directory and this script file are
# under the same parent directory.


import sys
import os

# keep the path of the suspicious file
suspicious_file_name = []

# the words that we are looking for
words = ["marijuana", "marihuana", "cannabis", "weed"]

# a function that check the name of a file
def check_name(path):
  # get the file base name
  file = os.path.basename(path)
  # case insensitive
  name = file.lower()
  for word in words:
    if word in name:
      suspicious_file_name.append(path)

  if "mary" in name and "jane" in name:
      suspicious_file_name.append(path)

# handle the given path
def handler(path):
  # if the path is a directory,
  # we recursively search it
  if os.path.isdir(path):
    for file in os.listdir(path):
      # get the updated path, then call itself recursively
      handler(os.path.join(path,file))
  # if it's a file name, then we call the check name function
  elif os.path.isfile(path):
    check_name(path)

def main():
  # no argument is provided
  if len(sys.argv) < 2:
    print("Please provide a base directory on the command line.")
    sys.exit(0)
  else:
    # get the base directory name
    base = sys.argv[1]
    # get the complete path of it
    path = os.path.abspath(base)
    # if the directory exists
    if os.path.exists(path):
      handler(path)
    # if the directory doesn't exist
    else:
      print("The directory does not exist.")
      sys.exit(0)

    # print out the result
    for item in suspicious_file_name:
      print(str(item))



if __name__ == "__main__":
  main()
