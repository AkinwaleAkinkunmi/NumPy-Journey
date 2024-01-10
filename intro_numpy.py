import numpy as np

#Initialising numpy arrays
a = np.array([[1,2,3,4,5,6,7], [8,9,10,11,12,13,14]])#You can specify the type to be stored 
print(a)

b = np.array([[1.0, 2.0, 3.0], [7.0, 3.0, 6.0]])
print(b)

#Getting dimensions
print(a.ndim)
print(b.ndim)

#Getting Shape
print(a.shape)
print(b.shape)

#Getting the type
print(a.dtype)

#Getting item size 
print(a.itemsize) #This shows how many bytes it is stored as

#Getting total size
print(a.nbytes)#This can also be written as a.size * a.itemsize

#Getting an element e.g 13
print(a[1, 5])

#Getting a specific row
print(a[0, :])

#Getting a specific column
print(a[:, -2])

#Getting elements while jumping at an interval
print(a[0, 1:6:2]) #[start_index: end_index: interval]

# 3-D example
d = np.array([[[1,2], [3,4]], [[5,6], [7,8]]])
print(d)

#Getting an element in a 3-D array
print(d[:, 1, :]) 


# All 0s matrix
print(np.zeros((2,2)))

# All 1s matrix
print(np.ones((4,2,2), dtype= 'int32'))

# Any other number
print(np.full((2,2), 99))

# Any other number - full like
print(np.full_like(a, 1)) # Or np.full(a.shape, 1)

# Arrays with random decimal numbers
print(np.random.rand(4,2))
print(np.random.random_sample(a.shape))

# Arrays with random integer numbers
print(np.random.randint(4, 7, size =(4,2)))

# Identity Matrix
print(np.identity(5))




