import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('./EyEDi/data/고용노동부_중대재해 발생이 규모별 동종업종 평균재해율 이상인 사업장_20211229.csv')
# print(df)
# 사고건수 높은 지역의 이름
loc = df['지역'].value_counts()

loc2 = df.groupby('지역')['규모별 동종업종 평균 재해율(퍼센트)'].max()
print(loc2)










