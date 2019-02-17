# Solution to problem 1
# Sum from and to a number

i = int (input("Enter a positive integer: "))

Total = 0

while i > 0:
    Total = Total + i
    i = i -1

print (Total)