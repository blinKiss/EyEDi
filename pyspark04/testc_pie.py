import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 인구비율 서울 경기 부산 광주
ratio = [42, 38, 12, 8]
cities = ['Seoul', 'Gyunggi', 'Busan', 'Gwangju']
plt.pie(ratio, labels=cities, autopct='%.1f%%', startangle=90, counterclock=False)
plt.show()

