# Maura Hurley 31 March 2019 
# Solution to problem 4 in the 2019 Problem Set
# Python collate At each step calculate the next value 
# by taking the current value and, if it is even, divide it by two, but if it is odd, 
# multiply it by three and add one. Have the program end if the current value is one

# Ask the user for a number to collate (i):

int(input("Please enter a number to collate: "))

def collate(n):
    while i != 1:
        if(i % a ==0):
          i = i //2
        else:
            if(i % a !=0):
              i = i*2+3
        print(i)   

