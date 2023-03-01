# 서울대기정보 2023년 1월~4월
# 구 별로 구분해서 각 구의 
# 초미세먼지 평균을 구하시오


#   micro_avg  /  micro_var   /  sup_mic_avg   /  sup_mic_var
import pandas as pd
import numpy as np


d1 = pd.read_csv('./EyEDi/data/서울시_기간별_시간평균_대기환경_정보_2020.01.csv')
d2 = pd.read_csv('./EyEDi/data/서울시_기간별_시간평균_대기환경_정보_2020.02.csv')
d3 = pd.read_csv('./EyEDi/data/서울시_기간별_시간평균_대기환경_정보_2020.03.csv')
d4 = pd.read_csv('./EyEDi/data/서울시_기간별_시간평균_대기환경_정보_2020.04.csv')

# 각 파일들이 데이터프레임 작업
df1 = pd.DataFrame(d1)
df2 = pd.DataFrame(d2)
df3 = pd.DataFrame(d3)
df4 = pd.DataFrame(d4)

temp = dft = pd.concat([df1, df2, df3, df4])


air = temp[['측정일시','측정소명','초미세먼지(㎍/㎥)','일산화탄소농도(ppm)']]
center = (temp['측정소명']).drop_duplicates()
# print(center) # --> 서울에 25개 구가 있음을 set으로 중복값을 걸러냄
# print(len(center))

# print(air.groupby('측정소명')['초미세먼지(㎍/㎥)'].mean())
print('20년도 1월 ~ 4월 자치구별 초미세먼지 농도\n')
mean = round(air.groupby('측정소명')['초미세먼지(㎍/㎥)'].mean(), 1).values
min = round(air.groupby('측정소명')['초미세먼지(㎍/㎥)'].min(), 1).values
max = round(air.groupby('측정소명')['초미세먼지(㎍/㎥)'].max(), 1).values
median = round(air.groupby('측정소명')['초미세먼지(㎍/㎥)'].median(), 1).values

air_df = pd.DataFrame({
    '측정소명' : center,
    '평균값' : mean,
    '최소값' : min,
    '최대값' : max,
    '중앙값' : median
})
print(air_df)
