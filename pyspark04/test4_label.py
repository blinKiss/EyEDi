import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import numpy as np

font_path = 'C:/Windows/Fonts/gulim.ttc'
myfont = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=myfont)

x = np.arange(0.0, 2*np.pi, 0.1)
y = np.sin(x)
# print(y)
plt.plot(x,y)
plt.xlabel('변수x')
plt.ylabel('변수y')
plt.show()

