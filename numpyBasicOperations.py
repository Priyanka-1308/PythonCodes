# Basic functions of array
import numpy as np

#creating array 2D
arr1 = np.array([[1, 2, 3],
                [4, 5, 6]])

#creating array 3D
arr2 = np.array([[3, 4, 5],
                [6, 7, 8],
                [10, 11, 12]])

print("Type of array:", type(arr1))
print("Type of array:", type(arr2))

print("Dimensions of array: ", arr1.ndim)
print("Dimensions of array: ", arr2.ndim)

print("Shape of the array: ", arr1.shape)
print("Shape of the array: ", arr2.shape)

print("Size of the array(no of elements): ", arr1.size)
print("Size of the array(no of elements): ", arr2.size)

print("Data type of elements: ", arr1.dtype)
print("Data type of elements: ", arr2.dtype)
