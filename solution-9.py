# Maura Hurley 31 March 2019
# Solution to problem 9 in the 2019 Problem Set
# Write a program that reads in a text file and outputs every second line. 
# The program should take the filename from an argument on the command line.

#Python Tutorial 7.2

with open("inishfree.txt", 'r') as f:
  for line in f.read().split("\n")[::2]:
    print(line)