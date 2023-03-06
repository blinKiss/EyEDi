import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0.0, 2*np.pi, 0.1) # 실수로 증가 (0.1씩 증가)
# print(x)
y = np.sin(x)
# plt.plot(x, y)
# plt.show()

for i in range(len(x)):
    print(x[i], ':', y[i])