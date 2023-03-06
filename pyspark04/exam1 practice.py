import matplotlib.pyplot as plt
import numpy as np

# # 윈도우 시스템 창 이름
# fig = plt.figure("radian sin / cos")

# # 그래프 제목 타이틀
# fig.suptitle('radian', fontsize=20)

# subplots_adjust(창과 plot의 거리 = 1에 가까울 수록 붙음)
# fig.subplots_adjust(top=0.8)
# plt.set_xlabel('rad', fontsize=10)
# plt.set_ylabel('sin', fontsize=10)


rad = np.arange(0.0, 2*np.pi, 0.1) # 실수로 증가
sin = np.sin(rad)
cos = np.cos(rad)
zeroline = 0 * rad

plt.plot(rad,sin, color='red', label='Sin')
plt.plot(rad,cos, color='blue', label='Cos')
plt.plot(rad,zeroline, color='brown')
# plt.plot(rad,z, color='blue')
plt.legend()


plt.title('Radian : Sin / Cos', loc='right')

plt.xlabel('Radian')
plt.ylabel('Sin / Cos')
plt.show()
