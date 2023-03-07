# figure 사용해서 그래프를 두개 만들고
# sin 그래프 그리고
# cos 그래프 그리시오

import matplotlib.pyplot as plt
import numpy as np

# 윈도우 시스템 창 이름
fig = plt.figure("radian sin / cos")

# 그래프 제목 타이틀
fig.suptitle('radian', fontsize=20)

# subplots_adjust(창과 plot의 거리 = 1에 가까울 수록 붙음)
fig.subplots_adjust(top=0.8)


rad = np.arange(0.0, 2*np.pi, 0.1) # 실수로 증가
x = np.sin(rad)
y = np.cos(rad)

plt1 = fig.add_subplot(1,2,1)
plt2 = fig.add_subplot(1,2,2)

plt1.plot(rad,x, color='red')

# 그래프 소제목 타이틀
plt1.set_title('rad/sin', fontsize=15)
# x축과 y축 이름
plt1.set_xlabel('rad', fontsize=10)
plt1.set_ylabel('sin', fontsize=10)

plt2.plot(rad,y, color='violet')


plt2.set_title('rad/cos', fontsize=15)
plt2.set_xlabel('rad', fontsize=10)
plt2.set_ylabel('cos', fontsize=10)

# plt1과 plt2의 가로 간격 조정 = wspace 세로 = hspace
plt.subplots_adjust(wspace=0.5)
plt.show()
