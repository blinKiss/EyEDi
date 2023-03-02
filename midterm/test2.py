import pandas as pd
import numpy as np

df = pd.read_csv('./EyEDi/data/서울교통공사_역별 일별 시간대별 승하차인원 정보_20221231.csv')
df['17-19시간대'] = df.loc[:, '17-18시간대'] + df.loc[:, '18-19시간대']
sta = df.groupby('역명')['17-19시간대'].sum()
print(sta.idxmax(), ':', sta.max())

