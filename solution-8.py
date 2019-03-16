# Maura Hurley 31 March 2019
# Solution to problem 8 in the 2019 Problem Set
# Output todays date in format "Monday,January 10th 2019 at 1:15pm". 

# Date formats "st", "nd", and "rd" is not available on python.
# Modified from [https://www.tutorialspoint.com/How-do-I-display-the-date-like-Aug-5th-using-python-s-strftime]
from datetime import datetime as dt
now = dt.now()
def suffix(day):
  suffix = ""
  if 4 <= day <= 20 or 24 <= day <= 30:
    suffix = "th"
  else:
    suffix = ["st", "nd", "rd"][day % 10 - 1]
  return suffix

# List of directives -[http://strftime.org/] 
# Remove leading zero in hour by placing "#" symbol in front of "I" 
# [https://stackoverflow.com/a/42709606] 
today = now.strftime("%A, %B %d" + suffix(now.day))+ now.strftime(" %Y at %#I:%M%p")

# Replace uppercase AM & PM with lower case).  
# Modified from [https://stackoverflow.com/a/30162144]
today = today.replace("PM","pm") 
today = today.replace("AM","am")
print(today)