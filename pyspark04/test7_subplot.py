import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import numpy as np

font_path = 'C:/Windows/Fonts/gulim.ttc'
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

fig = plt.figure()
sub_list = fig.add_subplot(1,1)


# sub=fig.add_subplot(1,1,1)
x = [1,2,3,4,5]
# y = [1,2,3,4,5]
# sub_list.plot(x)
# plt.show()