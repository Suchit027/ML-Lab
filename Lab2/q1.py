from matplotlib import pyplot as plt

fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])
x = [0, 100]
y = [0, 200]
ax.plot(x, y)
ax.set_title('title')
plt.xlabel('x')
plt.ylabel('y')
plt.show()