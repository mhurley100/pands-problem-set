# Maura Hurley 31 March 2019
# Solution to problem 2 in the 2019 Problem Set
# Is today a day that starts with "T"

# Import python module datetime and call it dt
import datetime as dt

# Create an if statement to ascertain if today is Tuesday (day 1)
if dt.datetime.today().weekday() == 1:
# Print today begins with T if day 1
  print("Yes today begins with a T") 
# If today is Thursday it is day 3 it starts with a "T".  Use elif to capture this rule
elif dt.datetime.today().weekday() == 3:
# Print today begins with T if day 3
 print("Yes - today begins with a T")
# Any other days do not start with "T" - Use "else" to catch all other days
else:
# Print today does not begin with a T (as not day 1 or 3)
  print("No - today does not begin with a T")