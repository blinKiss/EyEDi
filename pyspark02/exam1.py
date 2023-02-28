import pandas as pd

# name math kor
# kim 90 100
# choi 80 90
# yoon 70 90

# 각 사람의 성적합계를 구하고
# name math kor tot 컬럼으로 저장
# score_sum.csv
data = {
    'name' : ['Kim', 'Choi', 'Yoon'],
    'math' : [90, 80, 70],
    'kor' : [100, 90, 90]
}

df = pd.DataFrame(data)
df['tot'] = df.sum(axis=1)
df.to_csv('./data/score_sum.csv', index=False)
print(df)




