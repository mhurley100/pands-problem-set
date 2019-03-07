# Maura Hurley 31 March 2019
# Solution to problem 3 of the 2019 Problem Set
# Numbers between 1,000 and 10,000 divisible by 6 but not 12

# Name the divisors:

a,b = 6,12

# Create a range but increase upper end by 1 to ensure it is included

for i in range(1000,10001):
  # For integers in the range that are divisibe by 6 and not 12
  if(i % a ==0) and not (i % b ==0):
    print(i)
