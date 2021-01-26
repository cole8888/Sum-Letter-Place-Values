# Sums together the place values for every letter in the english alphabet.
# For instance, abc would be 1 + 2 + 3 = 6, 
# since a is the first letter in the alphabet, b is second and c is third.
# Capital letters are the same value as their lowercase counterparts.

# Cole Lightfoot - 25th January 2021

import subprocess
import sys

# Split the string into a list of chars
def split(word): 
    return [char for char in word]

# Get the input word, we need to switch the terminal mode to allow
# inputs greater than 4095 characters. We get the word and switch it back.
def getWord():
    subprocess.check_call(["stty","-icanon"]) # Comment me if input errors happen.
    inputStr = input("Word to test: ")
    subprocess.check_call(["stty","icanon"]) # Comment me if input errors happen.
    return inputStr

# Get the contents of a file and remove newline characters, then return as a string.
def getWordFromFile(f):
    try:
        with open(f, 'r') as file:
            data = file.read().replace('\n', '')
            return data
    except:
        raise FileNotFoundError("Could not find file ", f)

# Sum up the alphabetical place values for every letter in the
# given string and ignore any characters which are not letters.
def getCharSum(word):
    chars = [''] * len(word)
    chars = split(word)
    runningSum = 0

    # for all characters in the word, if the character is within the
    # range of a-z or A-Z get the ascii value and subtract the value
    # of the character before (a-1), and if it's a capital letter then
    # subtract (A-1).
    for i in chars:
        if(ord(i) < 91 and ord(i) > 64):
            runningSum += ord(i) - 64
        elif(ord(i) < 123 and ord(i) > 96):
            runningSum += ord(i) - 96
    return runningSum

# Run the program and print the output.
# If a file was entered in the arguments.
if(len(sys.argv) == 2):
    print(getCharSum(getWordFromFile(sys.argv[1])))
# If we want to enter it from the command line.
elif(len(sys.argv) == 1):
    print(getCharSum(getWord()))
else:
    raise ValueError("Too many command line arguments. sumLetterPlaceValues.py input.txt")
