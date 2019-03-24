# Maura Hurley 31 March 2019
# Solution to problem 10 of the 2019 Problem Set
# Display a plot of functions (x, x*x and x + x in the range[0-4])

# Import numpy for scientific computations and call it np
import numpy as np
# Import python data analysis library (pandas) and call it pd
import pandas as pd
#Matplotlib.pyplot needs to be imported for plotting purposes.  Call it plt
import matplotlib.pyplot as plt

# Determine series (0-4)
x = pd.Series([0,1,2,3,4])
#Adapted from [https://matplotlib.org/tutorials/introductory/pyplot.html]
# First plot is x
plt.plot(x)
# Second plot is x squared
plt.plot(x * x)
# Third plot is 2x
plt.plot(x + x)
# Show the plot
plt.show()