import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import numpy as np
import pandas as pd

font_path = 'C:/Windows/Fonts/gulim.ttc'
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

df = pd.read_csv('./EyEDi/data/해양수산부_해수욕장 개폐장일정_20220830.csv')

# 2021년 중에서 시도별 해수욕장갯수를 구해서 막대그래프로 출력하시오

df.columns = ['연도', '시도', '시군구', '해수욕장명', '개장일', '폐장일']
df2021 = df[df['연도'] == 2021]
df_cities = df2021['시도'].drop_duplicates()
# print(df2021)
# print(df_cities)
df_beach = [len(df2021[df2021['시도'] == city]) for city in df_cities]
beaches = sorted(df_beach, reverse=True)
cities = ['강원도', '전라남도', '충청남도', '경상남도', '경상북도', '제주특별자치도', '전라북도', '부산시', '인천시', '울산시']
# print(df_beach)

x = np.arange(len(cities))
y = beaches
plt.bar(x, y)
plt.xticks(x, cities)
plt.show()
