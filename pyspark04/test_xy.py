import matplotlib.pyplot as plt

x = range(0, 10)
y = [i*i*i for i in x]
plt.plot(x, y)
plt.show()
