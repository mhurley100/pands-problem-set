# Maura Hurley 31 March 2019 
# Solution to problem 4 in the 2019 Problem Set
# Python collate - at each step calculate the next value 
# Take the current value and, if it is even, divide it by two, but if it is odd, 
# multiply it by three and add one. Have the program end if the current value is one.

i = int(input("Please enter a positive integer: "))
i = accept_int()

# Create a loop that ends when i is not equal to 1:
while (i != 1):
# Check if the number is even and if it is divide by 2:
  if (i % 2 ==0):
    i = (i // 2)
# Modified stackoverflow to help print across [https://stackoverflow.com/a/10750004]
    print(i,end=' ')
# Check if the number is odd and if it is multiply by 3 and add 1:  
  else:
    i = (i * 3) + 1
# Modified stackoverflow to help print across [https://stackoverflow.com/a/10750004]
    print(i,end=' ') 