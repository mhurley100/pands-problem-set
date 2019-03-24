# Maura Hurley 31 March 2019
# Solution to Problem 1 of the 2019 Problem Set
# Aggregate a range from 0 to i

# "Try" and "except" handle exceptions [Modified from Python Tutorial 8.3 Handling Exceptions]
# Use "while" and "true" to determine if the input is valid
while True:
# Screen the user input by using try 
  try:
# Ask the user for a positive integer (i)
    i= int(input("Please enter a positive integer: "))
# If an integer is entered the except clause is skipped and the program moves on
    break
# If the user inputs text an exception is caused.  Force the user to enter a number:
  except ValueError:
# Tell the user that a positive integer has not been entered
    print("That's not a positive integer!")
# If no error is found the "except" clause is skipped

# Establish the start of the range (0) and call it start
start = 0
# Sum the Range from 0 to (i + 1) to include end of range and call it result
result = sum(range(start,i+1))
# If i is greater than or equal to 1 print the aggregated result
if i >=1:
# Print the result
  print("The Aggregate (from 0 to the positive integer) is", result)
# If a number less than 1 is entered ask the user to enter a positive number
else:
  print("That is not a positive integer greater than 0")