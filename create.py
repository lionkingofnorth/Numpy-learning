import numpy as np

# We create a 1D ndarray that contains only integers
x = np.array([1, 2, 3, 4, 5])

# We print x
print()
print('x = ', x)
print()

# We print information about x
print('x has dimensions:', x.shape)
print('x is an object of type:', type(x))
print('The elements in x are of type:', x.dtype)

# We create a rank 1 ndarray that only contains strings
y = np.array(['Hello', 'World'])

# We print x
print()
print('y = ', y)
print()

# We print information about x
print('y has dimensions:', y.shape)
print('y is an object of type:', type(y))
print('The elements in y are of type:', y.dtype)

# We create a rank 2 ndarray that only contains integers
Y = np.array([[1,2,3],[4,5,6],[7,8,9], [10,11,12]])

# We print Y
print()
print('Y = \n', Y)
print()

# We print information about Y
print('Y has dimensions:', Y.shape)
print('Y has a total of', Y.size, 'elements')
print('Y is an object of type:', type(Y))
print('The elements in Y are of type:', Y.dtype)

np.save("my_data",Y)