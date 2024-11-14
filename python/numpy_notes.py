#import package
import numpy as np

#Create a numpy array
print("Creating a numpy array")
s_list = ['sup','my','dude']
i_list = [1,2,3]
b_list = [True, False, True]
#1D
print("1D")
array_1D = np.array(s_list)
i_array = np.array(i_list)
print(array_1D, "\n",i_array)
#2D
print("2D")
array_2D = np.array([s_list, i_list])
print(array_2D)
#elementwise operations using arrays
print('You can use element wise operations(+,-,*,/) on arrays!')

#Numpy methods:
print("Numpy Methods")
#Shape gives you the dimensions of an array
print("Shape, dimensions of an array")
print(array_2D.shape)
#size gives you number of elements in the entire array
print("Size, number of elements in the entire array")
print(array_2D.size)

#Numpy Functions:
print("Numpy Functions")
#mean
print('Mean')
print(np.mean(i_array))
#standard deviation
print('Standard Deviation')
print(np.std(i_array))
#arange creates a numerical array with start, stop and step
print('Arange, create a numerical array')
print(np.arange(1, 13, 1)) #default step is 1
#transpose switches the rows and columns of a numpy arrray
print('Transpose, switch the rows and columns')
print(np.transpose(array_2D))

#Indexing a Numpy Array [row,column] (*python is zero-indexed)
print("Indexing")
#row index 1, column index 2
print("Row index 1, column index 2")
print(array_2D[1,2])
#slices also works. all row slice, column 3
print("All row slice, column 3")
print(array_2D[:,2])
#you can also index arrays with arrays
print("Index an array with an array")
indexing_array = np.array([0, 2])
print(array_1D[indexing_array])
#indexing with boolean arrays
print("Indexing with boolean arrays")
#example 1
print("Example 1")
b_array =   np.array(b_list)
print(array_1D[b_array])
#example 2
print("example 2")
indexing_array = i_array > np.mean(i_array)
print(indexing_array)
above_avg = i_array[indexing_array]
print(above_avg)