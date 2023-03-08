import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from wordcloud import WordCloud

df = pd.read_csv('./EyEDi/data/fruit_vegetable.csv')
# print(df)
wc = df.set_index('title').to_dict()['count']
# print(df2)

# 샘플 사전{dict} 데이터 생성
wcdata = {
    'Today' : 10,
    'we' : 5,
    'have' : 6,
    'learned' : 9,
    'how' : 8,
    'to' : 4,
    'find' : 3,
    'the' : 2,
    'frequency' : 1,
    'of' : 7
}


wordcloud = WordCloud(
    font_path = 'gulim', # font.ttf(mac의 경우 otf)의 경로 
    width = 400, # 너비
    height = 400, # 높이
    max_font_size = 100, # 가장 빈도수가 높은 단어의 폰트 사이즈
    background_color = 'white' # 배경색
).generate_from_frequencies(wc)


plt.figure()
plt.imshow(wordcloud)
plt.axis('off')
plt.show()