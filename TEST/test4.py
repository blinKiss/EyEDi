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
staLine = df3.groupby('역명')['호선'].max().reset_index()

# print(inAvg)
sta = df3.groupby('역명').sum().reset_index()
sta['호선'] = staLine['호선']
sort = sorted(zip(sta['역명'], sta['호선'], sta['일별 승차 인원']), key=lambda x: x[2], reverse=True)

sort2 = sort[0:10]

sta_top10 = [i[0] for i in sort2]
line_top10 = [j[1] for j in sort2]
count_top10 = [k[2] for k in sort2]

day = df[['수송일자']].drop_duplicates()

count2_top10 = [c/len(day) for c in count_top10]

# print(count2_top10)

x = np.arange(len(sta_top10))
y = count2_top10
plt.title('2022 최다 승차 수 역별 인원과 평균', loc='left')
plt.bar(x, y)
plt.xticks(x, sta_top10)
plt.show()
