import pandas as pd

df = pd.read_csv('./EyEDi/data/서울시_기간별_시간평균_대기환경_정보_2020.01.csv')
# print(df.columns)
df_slice = df[['측정소명', '미세먼지 24시간(㎍/㎥)']]
# print(df_slice)
cities = df_slice['측정소명'].drop_duplicates()
# print(cities)
city = sorted( cities )
# print(city)
city_sort = [(df_slice[df_slice['측정소명'] == c]) for c in city]
# print(city_sort)


# print('서울시 자치구별 미세먼지\n')
# for c in range(0, len(city_sort)):
#     print('{}의 일간 미세먼지 평균 : {}\n'.format(city[c], round(city_sort[c]['미세먼지 24시간(㎍/㎥)'].values.mean())))
df2 = pd.DataFrame({
    '측정소명' : city[:],
    '일간 미세먼지 평균' : round(df.groupby('측정소명')['미세먼지 24시간(㎍/㎥)'].mean()).values
})
print(df2)
# print(df.groupby('측정소명')['미세먼지 24시간(㎍/㎥)'].mean())
# data = {
#     '자치구명' : [],
#     '일간 미세먼지 평균 수치' : []
# }
# df2 = pd.DataFrame(data)
# df2['자치구명'] = city
# dust = []
# for c in range(0, len(city_sort)):
#     dust.append(round(city_sort[c]['미세먼지 24시간(㎍/㎥)'].values.mean(), 2))
# df2['일간 미세먼지 평균 수치'] = dust
# # print(df2)

# df2.to_csv('./EyEDi/data/서울시_자치구별_일간_미세먼지_평균_2020.01.csv', index=False)
# print(df2)


