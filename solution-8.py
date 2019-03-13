# Maura Hurley 31 March 2019
# Solution to problem 8 in the 2019 Problem Set
# Output todays date in format "Monday,January 10th 2019 at 1:15pm”. 

import datetime
# Stackoverflow for the codes:
print(datetime.datetime.now().strftime("%A,%B %d %Y at %I:%M%p"))