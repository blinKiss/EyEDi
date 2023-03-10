# test2.py
# 지하철 열차 승하차 데이터를 사용하여 (2022년 기준) 호선별 역별로 승차인원총수를 구하여
# 가장 승차가 많은 10개 역과 총승차인원수를 출력하시오
# https://www.data.go.kr/
# 서울교통공사_역별 일별 시간대별 승하차인원 정보 csv 파일 사용함
import pandas as pd
import numpy as np

df = pd.read_csv('./EyEDi/data/서울교통공사_역별 일별 시간대별 승하차인원 정보_20221231.csv')

df2 = df.loc[0: :2]
df_in = df2.iloc[:, 6:].fillna(0)
df2['일별 승차 인원'] = df_in.sum(axis=1)

df3 = df2[['호선', '역명', '일별 승차 인원']]
staLine = df3.groupby('역명')['호선'].max().reset_index()
sta = df3.groupby('역명').sum().reset_index()
sta['호선'] = staLine['호선']
sort = sorted(zip(sta['역명'], sta['호선'], sta['일별 승차 인원']), key=lambda x: x[2], reverse=True)
sort2 = sort[0:10]
sta_top10 = [i[0] for i in sort2]
line_top10 = [j[1] for j in sort2]
count_top10 = [k[2] for k in sort2]

df4 = pd.DataFrame({
    '호선' : line_top10,
    '역명' : sta_top10,
    '연간 승차 인원' : count_top10
})
df4.index = df4.index+1
print('연간 승차 인원 수 순위\n', df4)