import pandas as pd
import glob as glob

files = glob.glob('./EyEDi/data/소상공인시장진흥공단_상가(상권)정보_20221231/소상공인*.csv')
df_total = pd.DataFrame()
for file in files:
    df_temp = pd.read_csv(file, low_memory=False)
    df_total = pd.concat([df_total, df_temp], ignore_index=True)
df_slice = df_total[['상호명', '상권업종중분류명']]
df = df_slice[df_slice['상권업종중분류명'].str.contains('커피점/카페')]
df_m = df[df['상호명'].str.contains('메가커피')].count()
df_b = df[df['상호명'].str.contains('빽다방')].count()
df_s = df[df['상호명'].str.contains('스타벅스')].count()

# print(df_m[1])
print('전국의 커피점 매장 수\n메가커피 : {}, 빽다방 : {}, 스타벅스 : {}'.
      format(df_m[1], df_b[1], df_s[1]))