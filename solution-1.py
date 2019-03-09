# Maura Hurley 31 March 2019
# Solution to problem 1 in the 2019 Problem Set
# Aggregate a range from 1 to i

# Ask the user for a positive integer (i):
i= int (input("Please enter a positive integer: "))

# Establish the start of the range (0)
start = 0

# Increase i by 1 to ensure that the end of the range is included:
i = i + 1

# Sum the Range from 0 to i (result):
result = sum(range(start,i))

# If a negative number is entered ask the user to enter a positive number
# (i is incremented by 1 above so <= 1 is used)
if i <= 1:
  print("Please input a positive integer greater than 0")
# Print the result
else:
  print("The Aggregate (from 0 to the positive integer) is", result)