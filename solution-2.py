# Maura Hurley 31 March 2019
# Solution to problem 2
# Is today a day that starts with "T"

# Import python module datetime and call it dt
import datetime as dt

# Tuesday is day 3 therefore if weekday is day 3 then it starts with a "T"
if dt.datetime.today().weekday() == 3:
  print("Today starts with T") 

# Thursday is day 5 therefore if weekday is day 5 then it starts with a "T"
  if dt.datetime.today().weekday() == 5:
    print("Today starts with T")

# Any other days do not start with "T"
else:
  print("Today does not start with T")