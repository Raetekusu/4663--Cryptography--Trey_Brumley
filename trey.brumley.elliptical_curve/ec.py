###############################################
# Name: Trey Brumley
# Class: CMPS 4663 Cryptography
# Date: 04 August 2015
# Program 3 - Elliptical Curve
# Provided code for plotting used
###############################################

import numpy as np
import matplotlib.pyplot as plt

# Calculates X value of point 3
def getX3(s, x1, x2):
	x3 = (s*s) - x1 - x2
	return x3

# Calculates Y value of point 3	
def getY3(s, x1, y1, x3):
	y3 = y1 + (s*(x3-x1))
	return y3

def plot(a, b, x1, y1, x2, y2):
	#Converts values to int
	a = int(a)
	b = int(b)
	x1 = int(x1)
	y1 = int(y1)
	x2 = int(x2)
	y2 = int(y2)
	
	#Determines width and height of plot using the largest absolute X and Y values, plus 3
	w = x1 + 3
	if abs(x2) > abs(x1):
		w = x2 + 3
	h = y1 + 3
	if abs(y2) > abs(y1):
		h = y2 + 3
		
	# Calculates the slope
	s = (y1-y2)/(x1-x2)
	
	x3 = getX3(s, x1, x2)
	y3 = getY3(s, x1, y1, x3)
	
	# Updates height and width of the graph to account for Point 3
	if abs(x3) > abs(w):
		w = x3 + 3
	if abs(y3) > abs(h):
		h = y3 + 3

	# Annotate the plot with your name using width (w) and height (h) as your reference points.
	an1 = plt.annotate("Trey Brumley", xy=(-w+2 , h-2), xycoords="data",
				va="center", ha="center",
				bbox=dict(boxstyle="round", fc="w"))

	# This creates a mesh grid with values determined by width and height (w,h)
	# of the plot with increments of .0001 (1000j = .0001 or 5j = .05)
	y, x = np.ogrid[-h:h:1000j, -w:w:1000j]

	# Plot the curve (using matplotlib's countour function)
	# This drawing function applies a "function" described in the
	# 3rd parameter:  pow(y, 2) - ( pow(x, 3) - ax + b ) to all the
	# values in x and y.
	# The .ravel method turns the x and y grids into single dimensional arrays
	plt.contour(x.ravel(), y.ravel(), pow(y, 2) - ( pow(x, 3) - (a*x) + b ), [0])

	# Plot the points ('ro' = red, 'bo' = blue, 'yo'=yellow and so on)
	plt.plot(x1, y1,'ro')

	# Annotate point 1
	plt.annotate('x1,y1', xy=(x1, y1), xytext=(x1+1,y1+1),
			arrowprops=dict(arrowstyle="->",
			connectionstyle="arc3"),
			)

	plt.plot(x2, y2,'bo')

	# Annotate point 2
	plt.annotate('x2,y2', xy=(x2, y2), xytext=(x2+1,y2+1),
			arrowprops=dict(arrowstyle="->",
			connectionstyle="arc3"),
			)

	# Use a contour plot to draw the line (in pink) connecting our point.
	plt.contour(x.ravel(), y.ravel(), (y-y1)-s*(x-x1), [0],colors=('pink'))

	# I hard coded the third point, YOU will use good ol mathematics to find
	# the third point
	plt.plot(x3, y3,'yo')

	# Annotate point 3
	plt.annotate('x3,y3', xy=(x3, y3), xytext=(x3+1,y3+1),
			arrowprops=dict(arrowstyle="->",
			connectionstyle="arc3"),
			)

	# Show a grid background on our plot
	plt.grid()

	# Show the plot
	plt.show()
	
	return