import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import numpy as np
import pandas as pd

font_path = 'C:/Windows/Fonts/gulim.ttc'
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

scores = {
    'name' : ['유재석', '박명수', '정준하', '정형돈', '노홍철'],
    'math' : [75, 100, 65, 75, 100],
    'eng' : [90, 65, 60, 80, 85],
    'com' : [40, 35, 50, 85, 80]
    
}
df = pd.DataFrame(scores)
x = np.arange(len(df['name']))
y = df['math']
name = df['name']
fig = plt.figure()
sub1 = fig.add_subplot(1,2,1)
sub2 = fig.add_subplot(1,2,2)

sub1.bar(x - 0.2, y, width = 0.2, label = '수학', color='skyblue')
sub1.bar(x, df['eng'], width = 0.2, label = '영어', color='blueviolet')
sub1.bar(x + 0.2, df['com'], width = 0.2, label = '컴퓨터', color='orchid')

# 총합 평균 막대그래프로
df2 = df.drop(['name'], axis=1)
sum = df2.sum(axis=1)
avg = df2.mean(axis=1)
sub2.bar(x - 0.15, sum, width = 0.3, label = '총점', color='purple')
sub2.bar(x + 0.15, avg, width = 0.3, label = '평균', color='violet')

sub1.set_xticks(x, name)
sub2.set_xticks(x, name)
sub1.legend()
sub2.legend()
plt.show()


