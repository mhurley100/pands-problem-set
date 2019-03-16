# Maura Hurley 31 March 2019
# Solution to problem 9 in the 2019 Problem Set
# Write a program that reads in a text file and outputs every second line. 
# The program should take the filename from an argument on the command line.

# Modified using python tutorial 7.2.  [https://docs.python.org/3/tutorial/inputoutput.html]
# Open the text file and call it f:
with open("inishfree.txt", 'r') as f:

# Print every second line of the text file using f.read().split(). 
# Using the[::x] notation for "slicing", Modified from stackoverflow [https://stackoverflow.com/a/17645386]
  for line in f.read().split("\n")[::2]:
    print(line)