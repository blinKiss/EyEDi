import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import numpy as np

font_path = 'C:/Windows/Fonts/gulim.ttc'
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

x = [1,2,3,4,5]
y1 = [2,3,4,5,6]
y2 = [i*i for i in x]
y3 = [i*2 for i in x]

plt.plot(x, y1, label='더하기 1')
plt.plot(x, y2, label='제곱')
plt.plot(x, y3, label='곱하기 2')
plt.xlabel('1~5')
plt.ylabel('x 연산')
plt.legend(ncol=3)
plt.show()
