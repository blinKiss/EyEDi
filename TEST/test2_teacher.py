import pandas as pd

df = pd.read_csv('./EyEDi/data/서울교통공사_역별 일별 시간대별 승하차인원 정보_20221231.csv')
# print(df.shape[0])

#2022년만 추출은 넘어감

#승차 데이터 추출
df_brd = df[df['승하차구분']=='승차']
# print(df_brd.shape[0])

df_brd = df_brd.loc[:, df_brd.columns != '고유역번호(외부역코드)']
df_brd = df_brd.loc[:, df_brd.columns != '연번']
# print(df_brd.columns)

df_ysum = df_brd.groupby(['호선','역명']).sum() # 상하로 합계
df_total = pd.DataFrame(df_ysum.sum(axis=1)) # 가로로 합계
# print(df_total)
df_total.columns= ['total']
df_total2 = df_total.sort_values('total', ascending=False)
print(df_total2.head(10))
