import numpy as np

# array creation from list
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))

print(np.__version__)

# array creation from tuple
ar = np.array((10, 20, 30, 40, 50))
print(ar)


# 0-d array
arr0 = np.array(42)
print(arr0)

# 1-d array
arr1=np.array([100,200,300,400])
print(arr1)

# 2-d array
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2)

# 3-d array
arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr3)

# check number of dimensions
print(arr0.ndim)
print(arr1.ndim)
print(arr2.ndim)
print(arr3.ndim)

#  Access Array Elements
print(arr[0])       #output: 1
print(arr[4])       #output: 5
print(arr2[1,2])    #output: 6
print(arr3[1,0,2])  #output: 9

# Negative indexing
print(arr[-2])      #output: 4

# Slicing arrays
# Note: The result includes the start index, but excludes the end index.
print(arr[1:4])     #output: [2 3 4]
print(arr[:4])      #output: [1 2 3 4]
print(arr[2:])      #output: [3 4 5]
print(arr2[0:2, 1:3]) #output: [[2 3]
                      #         [5 6]]
