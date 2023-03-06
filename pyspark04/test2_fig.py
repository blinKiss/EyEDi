import matplotlib.pyplot as plt

fig = plt.figure()
fig2 = plt.figure()

subplt1 = fig.add_subplot(2,1,1)
subplt2 = fig.add_subplot(2,1,2)

x = range(1,100,2)
y1 = x
y2 = [i ** 2 for i in x] 
# print(x)

subplt1.plot(x,y1)
subplt2.plot(x,y2)
# plt.show()



subplt3 = fig2.add_subplot(1,2,1)
subplt4 = fig2.add_subplot(1,2,2)

x = range(2,100,2)
y = x

subplt3.plot(x,y)
subplt4.plot(x,y)
plt.show()
