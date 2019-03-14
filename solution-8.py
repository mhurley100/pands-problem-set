# Maura Hurley 31 March 2019
# Solution to problem 8 in the 2019 Problem Set
# Output todays date in format "Monday,January 10th 2019 at 1:15pm”. 

# Import datetime and call it dt
import datetime as dt

# Bring in todays date using  and call it today
# Strip out the leading zero's.  Modified from [https://stackoverflow.com/a/9526003]
#Used http://strftime.org/ for list of directives.

today = (dt.datetime.now().strftime("%A, %B %d %Y at %I:%#M%#p")).lstrip("0").replace(" 0", " ")
# Replace uppercase AM & PM with lower case).  
# Modified from [https://stackoverflow.com/a/30162144]
today = today.replace("PM","pm")
today = today.replace("AM","am")
print(today)