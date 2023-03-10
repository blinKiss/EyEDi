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
df3['호선'] = df3['호선'].astype(str)
df3['호선별 역명'] = df3['호선'] + '호선 ' + df3['역명']

staLine = df3.groupby('호선별 역명')['일별 승차 인원'].sum().reset_index()
sort = staLine.sort_values(by='일별 승차 인원', ascending=False)
sort2 = sort[0:10]
sort2[['호선', '역명']] = sort2['호선별 역명'].str.split('호선 ', expand=True)
sort3 = sort2[['호선', '역명', '일별 승차 인원']]
# print(sort3.columns)
sort3.rename(columns={'일별 승차 인원':'연간 승차 인원'})
sort3 = sort3.reset_index(drop=True)
sort3.index = sort3.index+1
sort3 = sort3.rename_axis('순위')
print('연간 승차 인원 수 순위\n', sort3)