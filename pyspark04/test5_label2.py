import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
# 2개의 그래프를 만듦
sub1 = fig.add_subplot(2,1,1)
sub2 = fig.add_subplot(2,1,2)

x = np.arange(0.0, 2*np.pi, 0.1)
y1 = [v*v for v in x]
y2 = np.sin(x)
sub1.plot(x, y1)
sub1.set_xlabel('rad', fontsize=10)
sub1.set_ylabel('rad^2', fontsize=10)

sub2.plot(x, y2)
sub2.set_xlabel('rad', fontsize=10)
sub2.set_ylabel('sin(rad)', fontsize=10)

plt.subplots_adjust(hspace=0.5)
plt.show()






