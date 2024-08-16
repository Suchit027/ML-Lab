import numpy as np

a = np.array([i for i in range(1, 10)]).reshape((3,3))
b = np.array([7, 8, 10, 4, 5, 6, 1, 2, 3]).reshape((3, 3))

add = a + b
print(add)
sub = a - b
print(sub)
print(f'sum of elements of matrix a {np.sum(a)}')
c = b.transpose()
print(f'sum of columns of matrix b')
for x in c:
    print(np.sum(x))
mul = a.dot(b)
sortarr = np.sort(add)
print(sortarr)