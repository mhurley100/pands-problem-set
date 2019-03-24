# Maura Hurley 31 March 2019
# Solution to problem 3 of the 2019 Problem Set
# Numbers between 1,000 and 10,000 divisible by 6 but not 12

# Name the divisors a (6) & b (12)
a,b = 6,12

# Establish integers in the range (1,000 to 10,000) using a for loop
# Increase the upper end by 1 to ensure 10,000 is included
for i in range(1000,(10000 + 1)):
# Check if integers are evenly divided by 6 and not evenly divided by 12
  if(i % a ==0) and (i % b !=0):
# Print those integers
    print(i)