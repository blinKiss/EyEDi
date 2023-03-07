# olympic-medals.csv
# 나라별로 금메달 갯수를 파이그래프로 그리기
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('./EyEDi/data/olympic-medals.csv')
df2 = df[['TEAM', 'Gold']]
# df2에서 열 Gold의 값이 0이 아닌 것만 새로 묶음
df2 = df2[df2.Gold != 0]
# print(df2)

# 금메달이 없는 국가를 제외한 모든 국가
# plt.pie(df2['Gold'], labels=df2['TEAM'], autopct='%.1f%%', startangle=90, counterclock=False)
# x = df2['TEAM']
# y = df2['Gold']
# plt.bar(x, y)
# plt.show()

# 금메달 수 10위권 국가
df3 = df[:10]
df3.loc[0, ['TEAM']] = ['USA']
df3.loc[1, ['TEAM']] = ['China']
df3.loc[3, ['TEAM']] = ['UK']
x = df3['TEAM']
y = df3['Gold']
# plt.bar(x, y)
plt.pie(df3['Gold'], labels=df3['TEAM'], autopct='%.1f%%', startangle=90, counterclock=False)

plt.show()