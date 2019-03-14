# Maura Hurley 31 March 2019
# Solution to problem 9 in the 2019 Problem Set
# Write a program that reads in a text file and outputs every second line. 
# The program should take the filename from an argument on the command line.

# Modified using python tutorial 7.2.  [https://docs.python.org/3/tutorial/inputoutput.html]
# Open the text file and call it f:
with open("inishfree.txt", 'r') as f:
# f.read reads the files contents.  Split the file at the end of each line.
# Print every second line of the text file using f.read().split() [https://stackoverflow.com/a/47062598]
  for line in f.read().split("\n")[::2]:
    print(line)