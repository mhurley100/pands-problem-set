# Maura Hurley 31 March 2019
# # Solution to problem 5 in the 2019 Problem Set
# Is it a prime number?

# A prime number is only divisible by itself and 1
# Ask the user for a number to check and call it n
n = int (input("Please enter a positive integer: "))

# A prime number is a number greater than one
if n > 1:
# Create a loop for numbers in the range 2 (as prime is > 1)to n 
  for i in range(2, n):
# if there is a number that divides, it is not a prime number
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
  print(n,"is not a prime number")