import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import numpy as np

font_path = 'C:/Windows/Fonts/gulim.ttc'
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

x = np.arange(5)
moral = [75, 85, 75, 75, 75]
kor = [100, 55, 65, 75, 85]
math = [75, 100, 65, 75, 100]
name = ['유재석', '박명수', '정준하', '정형돈', '노홍철']


plt.barh(x - 0.2, moral, height = 0.2, label = '도덕', color='skyblue')
plt.barh(x, kor, height = 0.2, label = '국어', color='blueviolet')
plt.barh(x + 0.2, math, height = 0.2, label = '수학', color='orchid')
plt.xlabel('예능성적')
plt.yticks(x, name)
plt.legend()
plt.show()