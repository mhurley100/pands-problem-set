# Maura Hurley 31 March 2019
# Solution to problem 7 in the 2019 Problem Set
# Square root of a postive floating number

# Ask the user to input a floating point number:

f= float (input("Please enter a positive floating number: "))

# If the floating point number is less than 0 ask the user to enter a positive number:
if f <= 0:
  print("Please input a posititve floating number")
# Use the sqrt function to calculate square root if the number entered is positive (f):
else:
# To square a number use **.  **.5 therefore is the square root.
# Use round to round,1 the square root to 1 decimal places
  result = round(f **(.5),1)
  print(f"The Square Root of {f} is approx. {result}.")