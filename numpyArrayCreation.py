#creating array using numpy
import numpy as np
import random

a = np.array([[1, 2, 4], [3, 6, 7]], dtype ='float')
print("Array created using list: ", a)

b = np.array((2, 3, 4, 5))
print("Array created using tuple: ", b)

c = np.zeros((2, 3), dtype="int")
print("all zeroes : ", c)

d = np.ones((2, 3), dtype="int")
print("all ones : ", d)

e = np.full((3, 3), 6, dtype='complex')
print("Mix array: ", e)

f = np.empty((2, 3), dtype="int")
print("Empty array: ", f)

g = np.random.random((2, 3))
print("Random array:", g)

h = np.random.randint(2, 10, (2, 2), dtype="int")
print("Random int: ", h)

l = np.random.rand((4))
print("Rand:", l)

j = np.arange(2, 100, 2)
print("Arrange is :", j)

k = np.linspace(0, 5, 10, dtype="int")
print("Linespace is: ", k)

arr3 = np.array([[1, 2, 3, 4],
                 [5, 6, 7, 8],
                 [9, 10, 11,12]
                ])

newarr = arr3.reshape(2, 3, 2)
print("Original array: ", arr3)
print("Changed array: ", newarr)

flatt = arr3.flatten()
print("Original array: ", arr3)
print("Flatten array: ", flatt)