"""
Linear Algebra:  Create a 2d vector v, using 10 random (Gaussian) scalars and plot the scalar-vectors on the same graph.   
What do you observe?
"""
#import numpy
import numpy as np
#import library to plot
import matplotlib.pyplot as plt

#set vector v as an array from numpy, 2=x in final x-position, 5=y in the final y-position of the array.
v = np.array ([2, 5])
#plot x from 0 to 1st position of array (x-coord=2) amd y from 0 to 2nd position of array (y-coord=5)
plt.plot ([0, v[0]],[0, v[1]])
#we now should have a vector from the origin to (2,5) as our vector
# setting color throughout loop of 10 random scalars within loop   Dont forget the colon!
for i in range (10):
# assign a numpy random to each scalar
	sc = np.random.randn ()
#multiply the scalar with the vector for scalvec=sc*vector
#a scalar times a vector array results in a scaled array, therefore scalevec will be an array with positions (x,y) -->([0,[0]],[0,[1]])
	scalevec = sc * v
#plot scalevec from origin to position of each scalevec using random color assigned each time
	plt.plot([0,scalevec[0]],[0,scalevec[1]],c=np.random.rand(3,))

#see the plot grid from matplotlib library
plt.grid ('on')
#sets the axis for the graph
plt.axis ([-8, 8, -8, 8]);
plt.show()