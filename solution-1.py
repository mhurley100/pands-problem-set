# Maura Hurley 31 March 2019
# Solution to problem 1
# Sum from and to a number

## Ask the user for the number to sum up to (call it i):

i = int (input("Please enter a positive integer greater than 0: "))

Total = 0

## Create a looping statement that decrements i by 1:

while i > 0:
    Total = Total + i
    i = i -1

print (Total)