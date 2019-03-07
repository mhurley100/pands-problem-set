# Maura Hurley 31 March 2019
# Solution to problem 2 in the 2019 Problem Set
# Is today a day that starts with "T"

# Import python module datetime and call it dt
import datetime as dt

# Tuesday is day 3 therefore if weekday is day 3 then it starts with a "T"
if dt.datetime.today().weekday() == 3:
  print("Today is a day that starts with T") 

# Thursday is day 5 therefore if weekday is day 5 then it starts with a "T"
  if dt.datetime.today().weekday() == 5:
    print("Today is a day that starts with T")

# Any other days do not start with "T"
else:
  print("Today does not start with T")