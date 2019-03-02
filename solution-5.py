# Maura Hurley 31 March 2019
# # Solution to problem 5
# Is it a prime number?

# A prime number is only divisible by itself and 1
# Ask the user for a number to check;

n = int (input("Please enter a positive integer: "))

# A prime number is greater than one
if n > 1:

# for numbers in range from 2 to n, if there is a number that divides,
# it is not a prime number
  for i in range(2, n):
    if (n % i) == 0:
      print(n, "is not a prime number")
      break

  else:
    print(n, "is a prime number")