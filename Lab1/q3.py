import  numpy as np

x = np.array([21, 64, 86, 22, 74, 55, 81, 79, 90, 89])
y = np.array([21, 7, 3, 45, 10, 29, 55, 4, 37, 18])

a1, a2 = [], []
for i in range(len(x)):
    if x[i] > y[i]:
        a1.append(i)
    elif x[i] == y[i]:
        a2.append(i)
a1 = np.array(a1)
a2 = np.array(a2)
print(a1)
print(a2)