# Maura Hurley 31 March 2019 
# Solution to problem 4 in the 2019 Problem Set
# Python collate - at each step calculate the next value 
# by taking the current value and, if it is even, divide it by two, but if it is odd, 
# multiply it by three and add one. Have the program end if the current value is one

# Ask the user for a number to collate (i):
i = int(input("Please enter a number to collate: "))

# Create a loop that ends when i is not equal to 1:
while (i != 1):
# Check if the numer is even and if it is divide by 2:
  if (i % 2 ==0):
    i = (i / 2)
    print(i)
# Check if the number is odd and if it is multiply by 3 and add 1:  
  else:
    i = (i * 3) + 1
    print (i)
