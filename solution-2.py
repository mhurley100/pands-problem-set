# Solution to problem 2
# Is today a day that starts with "T"

import datetime

if datetime.datetime.today().weekday() == 3:
  print("Today starts with T") 

  if datetime.datetime.today().weekday() == 5:
    print("Today starts with T")

else:
  print("Today does not start with T")