import subprocess

# Split the string into a list of chars
def split(word): 
    return [char for char in word]

# Get the input word, we need to switch the terminal mode to allow
# inputs greater than 4095 characters. We get the word and switch it back.
def getWord():
    subprocess.check_call(["stty","-icanon"])
    inputStr = input("Word to test: ")
    subprocess.check_call(["stty","icanon"])
    return inputStr

# Sum up the the alphabetical place values for every letter in the
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
print(getCharSum(getWord()))