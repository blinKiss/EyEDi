# test4.py
# test2에서 나온 결과 중 역들의 하루 평균 승차 수
# 를 matplotlib 를 사용하여 막대 그래프로 시각화 하시오
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import numpy as np
import pandas as pd

font_path = 'C:/Windows/Fonts/gulim.ttc'
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

df = pd.read_csv('./EyEDi/data/서울교통공사_역별 일별 시간대별 승하차인원 정보_20221231.csv')

df2 = df.loc[0: :2]
df_in = df2.iloc[:, 6:].fillna(0)
df2['일별 승차 인원'] = df_in.sum(axis=1)

df3 = df2[['호선', '역명', '일별 승차 인원']]
df4 = df3.groupby(['호선', '역명']).sum()
sort = df4.sort_values('일별 승차 인원', ascending=False).reset_index()
sort.rename(columns={'일별 승차 인원' : '연간 승차 인원'}, inplace=True)
sort2 = sort[0:10]
sort2.index = sort2.index+1
sort2 = sort2.rename_axis('순위')

day = df[['수송일자']].drop_duplicates()

count = [round(c/len(day), 1) for c in sort2.loc[:, '연간 승차 인원']]
# print(count)

x = np.arange(len(sort2))
y = count
plt.title('2022 최다 승차 수 역별 인원과 평균', loc='left')
plt.bar(x, y)
plt.xticks(x, sort2.loc[:, '역명'])
plt.show()
