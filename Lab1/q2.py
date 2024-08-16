import numpy as np

arr = np.arange(9)
for i in range(len(arr)):
    if arr[i] % 2 != 0:
        arr[i] = -1
print(arr)