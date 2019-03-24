# Maura Hurley 31 March 2019
# # Solution to problem 5 in the 2019 Problem Set
# Is it a prime number (divisible by itself and 1)?

# Use "while" and "true" to determine if the input is valid. [Python Tutorial 8.3 Handling Exceptions]
while True:
# Screen the user input by using try 
  try:  
# Ask the user for a number to check and call it n
    n = int (input("Please enter a positive integer: "))
# If an integer is entered the except clause is skipped and the program moves on
    break
# If the user inputs a letter an error message is returned
  except ValueError:
# Tell the user that the input is not numeric
    print("That's not a positive integer!")

# Create the first test criteria using "if" - is the number greater than one?
if n > 1:
# If the above test is passed, integers in the range 2 (as prime is > 1) to n are determined
  for i in range(2, n):
# if there is a number in that range that divides evenly, it is not a prime number
    if (n % i) == 0:
# Print that n is not a prime number as it has it has a divisor
      print(n, "is not a prime number")
# Terminate the loop
      break
# If the number does not have a divisor use else to assign it as a prime number
  else:
# loop did not find a factor:
    print(n, "is a prime number")
# If number entered is less than or equal to 1, it is not a prime number:
else:
# Tell the user that the number entered is not prime (as less than or equal to one)
  print(n,"is not a prime number - input has to be greater than 1") 