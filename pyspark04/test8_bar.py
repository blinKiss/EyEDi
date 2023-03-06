import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import numpy as np

font_path = 'C:/Windows/Fonts/gulim.ttc'
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)



x = np.arange(5)
y = [90, 80, 90, 60, 70]
y2 = [80, 90, 60, 70, 90]
name = ['Kim', 'Lee', 'Park', 'Choi', 'Jeong']

plt.bar(x - 0.15, y, width = 0.3)
plt.bar(x + 0.15, y2, width = 0.3)
plt.xticks(x, name)
plt.show()