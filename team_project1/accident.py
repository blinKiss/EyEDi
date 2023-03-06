import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import numpy as np
import pandas as pd

font_path = 'C:/Windows/Fonts/gulim.ttc'
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

df = pd.read_csv('./EyEDi/data/고용노동부_중대재해 발생이 규모별 동종업종 평균재해율 이상인 사업장_20211229.csv')
# 사고건수 높은 지역순
loc = df['지역'].value_counts()
# 동종 평균 재해율 높은 순
loc_acd_per = df.groupby('지역')['규모별 동종업종 평균 재해율(퍼센트)'].max()

idx = np.arange(len(loc))

fig = plt.figure()

sub1 = fig.add_subplot(2,2,1)
sub2 = fig.add_subplot(2,2,2)
sub3 = fig.add_subplot(2,2,3)
sub4 = fig.add_subplot(2,2,4)

sub1.bar(idx , loc)
sub1.set_xticks(idx, loc.index)

sub2.bar(idx, loc_acd_per)
sub2.set_xticks(idx, loc_acd_per.index)
plt.show()





