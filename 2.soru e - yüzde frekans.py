import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

#define data values
data = [514, 476, 497, 511, 484, 513, 471, 470, 441, 466, 443, 481, 502, 528, 459, 548, 521, 517,463, 478, 473, 514, 542, 519, 522, 523, 546, 487, 486, 473, 527, 470, 440, 564, 499, 523,484, 463, 461, 437, 555, 525, 461, 539, 466, 470, 486, 490, 543, 519]


#create relative frequency histogram with percentages on y-axis
fig = plt.figure()
ax = fig.add_subplot(111)
ax.hist(data, edgecolor='black', weights=np.ones_like(data)*100 / len(data))
ax.yaxis.set_major_formatter(PercentFormatter())
plt.xlabel('Veri')
plt.ylabel('Yüzde Frekans')
plt.title('Verilerin Yüzde Frekansları Histogramı')
plt.show()

