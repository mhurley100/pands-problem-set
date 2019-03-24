# Maura Hurley 31 March 2019
# Solution to problem 7 in the 2019 Problem Set
# Square root of a postive floating number

# Ask the user to input a floating point number and an approximation (integer):

f= float (input("Please enter a positive floating number: "))
approx= int (input("Please enter an approximation(integer): "))

# For integers in the range approx, a better approximation is determined using a looping statement
for i in range(approx):
# Adapted the formula (better =  1/2 * (approx + n/approx)) to calculate approximate.  Call it ans
# Adapted from [http://interactivepython.org/runestone/static/thinkcspy/MoreAboutIteration/Newton%27sMethod.html]
  ans = 0.5 * (approx + f/approx)
# This better approximate is now the answer
  approx = ans
# Use round to round the result of the square root to 1 decimal place
  ans = round(ans,1)
# Print the approximate square root of the initial floating point number entered
print(f"The Square Root of {f} is approx. {ans}.")