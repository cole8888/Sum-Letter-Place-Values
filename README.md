# Sum-Letter-Place-Values
Simple python program to calculate the sum of the alphabetical order of every letter in a string (a = 1, b = 2, z = 26, etc...).

The program can read the contents of a file mentioned on the command line.
If no file is entered it can accept an input string from the command line. It will switch the terminal mode in order to allow inputs greater than 4095 characters, this may cause issues on some systems so just comment out those lines, I have labeled them in the file. Make sure your string is short enough for your terminal to support it if you do this.

It ignores invalid characters other than new line characters, make sure you remove any of them prior.

Tested on Ubuntu Linux 20.04 using python 3.8.

To run it:

python3 sumLetterPlaceValues.py

or

python3 sumLetterPlaceValues.py input.txt

Example:

![Example](Screenshot_20200812_023421.png)
