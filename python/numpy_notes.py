#import package
import numpy as np

#Create a numpy array
list_1 = ['sup','my','dude']
list_2 = [1,2,3]
#1D
array_1D = np.array(list_2)
#2D
array_2D = np.array([list_1, list_2])

#Numpy methods:
#Shape gives you the dimensions of an array
print(array_2D.shape)
#size gives you number of elements in the entire array
print(array_2D.size)

#Numpy Functions:
#mean
print(np.mean(array_1D))
#standard deviation
print(np.std(array_1D))
#arange creates a numerical array with start, stop and step
print(np.arange(1, 13, 1)) #default step is 1
#transpose switches the rows and columns of a numpy arrray
print(np.transpose(array_2D))

#Indexing a Numpy Array [row,column] (*python is zero-indexed)
#row index 1, column index 2
print(array_2D[1,2])
#slices also works. all row slice, column 3
print(array_2D[:,2])
#you can also index arrays with arrays
indexing_array = np.array([0,2])
print(array_1D[indexing_array])
#indexing with boolean arrays
