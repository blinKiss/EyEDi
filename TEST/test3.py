# test3.py
# 한국교통안전공단 자동차 결함 데이터를 이용하여
# https://www.data.go.kr/data/3048950/fileData.do
# 리콜사유에 브레이크 또는 엔진오일 이라는 글자가 포함된 리콜 건을
# 제조사별로 리콜수를 출력하시오
import pandas as pd

df = pd.read_csv('./EyEDi/data/한국교통안전공단_자동차결함 리콜현황_20211231.csv')
df_recall = df[['제작자', '리콜사유']]
df_bAndO = df_recall[df_recall['리콜사유'].str.contains('브레이크|엔진오일')]
print('제조사 별 리콜 수\n',df_bAndO['제작자'].value_counts())

