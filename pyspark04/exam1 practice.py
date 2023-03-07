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
# print(df_beach)
# print(df_cities)
df_zip = sorted(zip(df_cities, df_beach), key=lambda x: x[1], reverse=True)
# print(df_zip)
cities = [i[0] for i in df_zip]
beaches = [j[1] for j in df_zip]

x = np.arange(len(df_cities))
y = beaches
plt.bar(x, y)
plt.xticks(x, cities)
plt.show()