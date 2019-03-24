# Maura Hurley 31 March 2019
# Solution to problem 9 in the 2019 Problem Set
# Write a program that reads in a text file and outputs every second line. 
# The program should take the filename from an argument on the command line.

# To take arguments from the command line, sys needs to be imported
import sys

# The number of commands needs to be 2 (as filename needs to be present)
if len(sys.argv) != 2:
# Tell the user to enter a filename
  print("A single filename needs to be entered!")
# If the number of arguments is equal to 2, the program can proceed using else
else:
# sys.argv[1] is the second argument on the CLI.  Call it filename.
  filename = sys.argv[1]
# Print the filename entered by the user [Inishfree.txt is saved for test purposes]
  print(filename)
  
# Use try and except to highlight input errors by the user
try:
# Modified using python tutorial 7.2.  [https://docs.python.org/3/tutorial/inputoutput.html]
# Open filename (user file on the CLI) and call it f:
  with open(filename, 'r') as f:
# Print every second line of the text file using f.read().split(). 
# Using the[::x] notation for "slicing", Modified from stackoverflow [https://stackoverflow.com/a/17645386]
    for line in f.read().split("\n")[::2]:
# Print every second line
      print(line)
# If the file is not found return an error message
except FileNotFoundError:
# Tell the user that a valid filename has not been entered
  print("That's not a valid filename!")
# If the name of the file is not entered correctly return an error message
except NameError:
# Tell the user that a valid filename has not been entered
  print("A valid filename needs to be entered")