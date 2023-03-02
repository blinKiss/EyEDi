import pandas as pd

df = pd.read_csv('./EyEDi/data/한국교통안전공단_자동차결함 리콜현황_20211231.csv')
df_slice = df['제작자'].value_counts()
print('제조사별 리콜 수\n',df_slice)