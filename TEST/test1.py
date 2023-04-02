# test1.py
# 전국 상권 데이터를 모두 읽어서 '상권업종중분류명' 이 '종합소매점' 인 데이터 중에서
# GS25, CU, 세븐일레븐 편의점의 전국의 각각 총갯수를 각각 구하시오
# https://www.data.go.kr/
# 소상공인시장진흥공단_상가(상권)정보 csv 데이터 파일 사용함
import pandas as pd
import glob as glob

files = glob.glob('./EyEDi/data/소상공인시장진흥공단_상가(상권)정보_20221231/소상공인*.csv')
df_total = pd.DataFrame()
for file in files:
    df_temp = pd.read_csv(file, low_memory=False)
    df_total = pd.concat([df_total, df_temp], ignore_index=True)
df_slice = df_total[['상호명', '상권업종중분류명']]
df = df_slice[df_slice['상권업종중분류명'].str.contains('종합소매점')]
df_g = df[df['상호명'].str.contains('GS25')].count()
df_c = df[df['상호명'].str.contains('CU')].count()
df_s = df[df['상호명'].str.contains('세븐일레븐')].count()

# print(df_m[1])
print('전국의 편의점 매장 수\nGS25 : {}, CU : {}, 세븐일레븐 : {}'.
      format(df_g[1], df_c[1], df_s[1]))
