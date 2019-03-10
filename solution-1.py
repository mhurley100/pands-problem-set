# Maura Hurley 31 March 2019
# Solution to problem 1 in the 2019 Problem Set
# Aggregate a range from 1 to i

# Ask the user for a positive integer (i):
i= int (input("Please enter a positive integer: "))

# Establish the start of the range (0) and call it start:
start = 0

# Sum the Range from 0 to (i + 1) to include end of range and call it result:
result = sum(range(start,i+1))

# If i is greater than or equal to 1 print the aggregated result:
if i >=1:
# Print the result
  print("The Aggregate (from 0 to the positive integer) is", result)

# If a number less than 1 is entered ask the user to enter a positive number
else:
  print("Please input a positive integer greater than 0")