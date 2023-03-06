import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import numpy as np
import pandas as pd
import glob as glob

font_path = 'C:/Windows/Fonts/gulim.ttc'
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)


files = glob.glob('./EyEDi/data/소상공인시장진흥공단_상가(상권)정보_20221231/소상*.csv')
df_total = pd.DataFrame()

for file in files:
    if('서울' in file or '경기' in file or '인천' in file or '부산' in file or '광주' in file):
        df_temp = pd.read_csv(file, low_memory='False')
        df_total = pd.concat([df_total, df_temp], ignore_index=True)


df_cafe = df_total[df_total['상권업종중분류명'] == '커피점/카페']
# print(df_cafe)
dfv = df_total[['상호명', '상권업종대분류명', '상권업종중분류명', '시도명']].fillna(' ')
cities = ['서울특별시', '인천광역시', '경기도', '광주광역시', '부산광역시']
df_paikcoff = dfv[dfv['상호명'].str.contains('빽다방')]
df_paikcoff2 = dfv[dfv['상호명'] == '백다방']
df_paikcoff3 = pd.concat(df_paikcoff, df_paikcoff2)
df_paikcoff_not_cafe = df_paikcoff3[df_paikcoff3['상권업종중분류명']!='커피점/카페']
# print(df_paikcoff_not_cafe)
city_cnt = [len(df_paikcoff3[df_paikcoff3['시도명']==city]) for city in cities]
print(city_cnt)

x = np.arange(len(cities))
y = city_cnt
plt.bar(x, y)
plt.xticks(x, cities)
plt.show()



