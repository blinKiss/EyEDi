import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# 점수 90 A 80 B ~ 60 미만 F
# grade 컬럼을 만들어서 학점을 저장

scores = {
    'name' : ['Kim', 'Lee', 'Park', 'Choi', 'Jeong', 'Kang', 'Jo', 'Yoon', 'Jang', 'Lim'],
    'math' : [80, 70, 60, 90, 80, 55, 80, 75, 90, 85]
}
df = pd.DataFrame(scores)
# print(df['name'])

# 학점 비율을 파이그래프로 출력하시오

# 인터넷 pd.cut 예제
# ages = [0, 10, 15, 13, 21, 23, 37, 31, 43, 80, 61, 20, 41, 32, 100]
# bins = [0, 15, 25, 35, 60, 100]
# labels = ['어린이', '청년', '장년', '중년', '노년']
# cuts = pd.cut(ages, bins, right=False, labels=labels)
# cuts
# right=True로 설정하면 60 < 노년 <= 100으로 설정될 것이며, 
# NaN이 마지막에 발생되지 않고 100은 노년으로 구분될 것입니다.
# right=False는 60 <= 노년 < 100
# [어린이, 어린이, 청년, 어린이, 청년, ..., 노년, 청년, 중년, 장년, NaN]
# Length: 15
# Categories (5, object): [어린이 < 청년 < 장년 < 중년 < 노년]

# 내꺼
math = df['math']
bins = [0, 60, 70, 80, 90, 101]
grade = ['A', 'B', 'C', 'D', 'F']
cuts = pd.cut(math, bins, right=False, labels=grade) # pd.cut(내점수, 점수범위와 나눌곳, 부등호, 나눈 후 붙여줄 값?)
df['grade'] = cuts
df_grade = df['grade'].value_counts()
# print(df_grade)
plt.pie(df_grade, labels=grade, autopct='%.1f%%', startangle=90, counterclock=False)
plt.show()



# 선생님 답
# math = df['math']
# grade = []
# for i in math:
#     if(i >= 90):
#         grade.append('A')
#     elif(i >= 80):
#         grade.append('B')
#     elif(i >= 70):
#         grade.append('C')
#     elif(i >= 60):
#         grade.append('D')
#     else:
#         grade.append('F')
# # print(grade)
# df['grade'] = grade
# grade_list = ['A', 'B', 'C', 'D', 'F']
# df_grade = df.groupby('grade').count()['math']
# plt.pie(df_grade, labels=grade_list, autopct='%.1f%%', startangle=90, counterclock=False)
# plt.show()







