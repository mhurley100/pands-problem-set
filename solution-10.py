# Maura Hurley 31 March 2019
# Solution to problem 10 of the 2019 Problem Set
# Display a plot of functions (x, x^x and 2x in the range[0-4])

# Import numpy for scientific computations and call it np
import numpy as np
# Import python data analysis library (pandas) and call it pd
import pandas as pd
#Matplotlib.pyplot needs to be imported for plotting purposes.  Call it plt
import matplotlib.pyplot as plt

# Determine series (0-4)
x = pd.Series([0,1,2,3,4])
#Adapted from [https://matplotlib.org/tutorials/introductory/pyplot.html]
# First plot is x - plot in red dots and line width 3mm
plt.plot(x, 'r--', linewidth= 3.0)
# Second plot is x squared - plot in green dots and line width 3mm
plt.plot(x * x, 'g--',linewidth= 3.0)
# Third plot is 2x - plot in blue dots and line width 3mm
plt.plot(2 * x, 'b--', linewidth= 3.0)       
# Create header for display, modified from [https://www.kaggle.com/andyxie/matplotlib-plot-multiple-lines]
plt.title("Plot of Functions", fontsize=16, fontweight='bold')
# Print X label and call it X axis, modified from [https://www.kaggle.com/andyxie/matplotlib-plot-multiple-lines]
plt.xlabel("X Axis")
# Print Y label and call it Y axis, modified from [https://www.kaggle.com/andyxie/matplotlib-plot-multiple-lines]
plt.ylabel("Y Axis")
# Print legend, modified from Stackoverflow [https://stackoverflow.com/a/19125863]
plt.legend(['y = x', 'y = x^x', 'y = 2^x',], loc='upper left')
# Show the plot
plt.show()