import  numpy as np

arr = np.arange(9)
# -1 in reshape is to let the reshape function the no. of elements in last dimension on its own
arr = arr.reshape((3, -1))
print(arr)