import numpy as np

"""
# When loading an array from a file, 
# make sure you include the name of the file together with the extension .npy, 
# otherwise you will get an error.
"""
y=np.load("my_data.npy")

print()
print("y:{}".format(y))

