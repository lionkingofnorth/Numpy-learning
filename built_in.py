import numpy as np


"""
built-in function test
"""

X=np.zeros((3,4))

# We print X
print()
print('X = \n', X)
print()

# We print information about X
print('X has dimensions:', X.shape)
print('X is an object of type:', type(X))
print('The elements in X are of type:', X.dtype)

#ones create one element array
Z=np.ones((3,2),np.int8)

# We print X
print()
print('Z = \n', Z)
print()

# We print information about X
print('Z has dimensions:', Z.shape)
print('Z is an object of type:', type(Z))
print('The elements in Z are of type:', Z.dtype)






"""
#FULL  function test
All element is assigned with given number
"""

y=np.full((3,3),12,np.float)

# We print X
print()
print('y = \n', y)
print()

# We print information about X
print('X has dimensions:', y.shape)
print('X is an object of type:', type(y))
print('The elements in X are of type:', y.dtype)


"""
#EYE  function test
function np.eye(N) creates a square N x N ndarray 
corresponding to the Identity matrix. Since all Identity Matrices are square, the np.eye() function only takes a single integer as an argument.
"""

# y=np.ones((3,2),np.int8)
aa=np.eye(5)
# We print X
print()
print('aa = \n', aa)
print()

# We print information about X
print('aa has dimensions:', aa.shape)
print('aa is an object of type:', type(aa))
print('The elements in aa are of type:', aa.dtype)

"""
#EYE  function test
function np.eye(N) creates a square N x N ndarray 
corresponding to the Identity matrix. Since all Identity Matrices are square, the np.eye() function only takes a single integer as an argument.
"""

# y=np.ones((3,2),np.int8)
bb=np.diag([10,12,14,16])
# We print X
print()
print('bb = \n', bb)
print()

# We print information about X
print('bb has dimensions:', bb.shape)
print('bb is an object of type:', type(bb))
print('The elements in bb are of type:', bb.dtype)


cc=np.arange(12)
# bb=np.diag([10,12,14,16])
# We print X
print()
print('bb = \n', cc)
print()

# We print information about X
print('bb has dimensions:', cc.shape)
print('bb is an object of type:', type(cc))
print('The elements in bb are of type:', cc.dtype)


toto=np.random.randint(1,50,7)
print("TOTO:{}".format(toto))