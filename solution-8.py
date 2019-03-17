# Maura Hurley 31 March 2019
# Solution to problem 8 in the 2019 Problem Set
# Output todays date in format "Monday,January 10th 2019 at 1:15pm". 

# Date formats "st", "nd", and "rd" is not available on python.
# Modified from [https://www.tutorialspoint.com/How-do-I-display-the-date-like-Aug-5th-using-python-s-strftime#Rajendra-Dharmkar]
# Import datetime and call it dt
from datetime import datetime as dt
# dt.now() is called now
now = dt.now()
# Define suffix(day)
def suffix(day):
# If suffix is not contained in the if statement, assign "th" as the default
  suffix = ""
# If day is in range 1-3, 20-23 or 30+ it needs a suffic
  if 4 <= day <= 20 or 24 <= day <= 30:
# "th" is assinged if not in range 1-3, 20-23 or 30+ 
    suffix = "th"
# if days are in range 1-3, 20-23 or 30+ use else to determine the suffix
  else:
# Take one from the suffix to adjust the range i.e 3 is 2
    suffix = ["st", "nd", "rd"][day % 10 - 1]
# return relevant suffix i.e. "st", "nd" or "rd"
  return suffix

# List of directives -[http://strftime.org/] 
# Remove leading zero in hour by placing "#" symbol in front of "I" 
# [https://stackoverflow.com/a/42709606] 
today = now.strftime("%A, %B %d" + suffix(now.day))+ now.strftime(" %Y at %#I:%M%p")

# Replace uppercase AM & PM with lower case).  
# Modified from [https://stackoverflow.com/a/30162144]
today = today.replace("PM","pm") 
today = today.replace("AM","am")
# Print todays date
print(today)