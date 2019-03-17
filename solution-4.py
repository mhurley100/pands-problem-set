# Maura Hurley 31 March 2019 
# Solution to problem 4 in the 2019 Problem Set
# Python collatz

i = int(input("Please enter a positive integer: "))
# Name the integer entered "start" 
start = i
# Print so it appears first on the output
# Modified stackoverflow to print across [https://stackoverflow.com/a/10750004]
print(start,end=' ')

# Create a looping statement that ends when i is not equal to 1
while (i != 1):
# Check if the number is even and if it is divide by 2
  if (i % 2 ==0):
    i = (i // 2)
# Print so it appears next on the output
    print(i,end=' ')
# If the number is not even, it is odd.  Use else to verify if odd
# If odd multiply by 3 and add 1 
  else:
    i = (i * 3) + 1
# Print so it appears next on the output
    print(i,end=' ') 