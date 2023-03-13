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
df4 = df3.groupby(['호선', '역명']).sum()
sort = df4.sort_values('일별 승차 인원', ascending=False).reset_index()
sort.rename(columns={'일별 승차 인원' : '연간 승차 인원'}, inplace=True)
sort2 = sort[0:10]
# print(sort2)
sort2.index = sort2.index+1
sort2 = sort2.rename_axis('순위')
print('연간 승차 인원 수 순위\n', sort2)
