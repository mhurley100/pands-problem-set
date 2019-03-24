# Maura Hurley 31 March 2019 
# Solution to problem 4 in the 2019 Problem Set
# Python collatz

# Use a while loop to determine that the input is valid [Python Tutorial 8.3 Handling Exceptions]
while True:
# Using "try" and "except" to determine if the user input is an integer
  try:
# Ask the user for a positive integer (i)
    i= int(input("Please enter a positive integer: "))
# If an integer is entered the except clause is skipped and the program moves on
    break
# If the user inputs a letter an error message is returned
  except ValueError:
    print("That's not a positive integer!")
# If no error is found the "except" clause is skipped

# Name the integer entered "start" 
start = i  
# Create an if statement to determine if i is greater than 1.
if i < 0:
# If an integer less than 0 is entered the user is informed
  print("That's not a positive integer!")
# If the integer entered is greater than 0 the program moves on using else
else:
# Print so it appears first on the output.  Modified stackoverflow to print across [https://stackoverflow.com/a/10750004]
  print(start,end=' ')
# Create a looping statement that ends when i is equal and greater than 1
  while (i != 1) and (i > 1):
# Check if the number is even 
    if (i % 2 ==0):
# If the number is even divide by 2
      i = (i // 2)
# Print so it appears next on the output
      print(i,end=' ')
# If the number is not even, it is odd. Use else to move the program to the next rule 
    else:
# If the number is odd multiply by 3 and add 1
      i = (i * 3) + 1
# Print so it appears next on the output
      print(i,end=' ') 