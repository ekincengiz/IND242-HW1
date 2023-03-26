from matplotlib import pyplot as plt
import numpy as np
#Veri setini oluşturuyoruz
a=np.array([514, 476, 497, 511, 484, 513, 471, 470, 441, 466, 443, 481, 502, 528, 459, 548, 521, 517,463, 478, 473, 514, 542, 519, 522, 523, 546, 487, 486, 473, 527, 470, 440, 564, 499, 523,484, 463, 461, 437, 555, 525, 461, 539, 466, 470, 486, 490, 543, 519])
#Histogramı oluşturuyoruz
fig, ax = plt.subplots(figsize=(8,6))
ax.hist(a, bins=[437,453,469,485,501,517,533,549,565], color="purple", edgecolor="black", fill="True")
# Eksen etiketleri ve başlığı
plt.xlabel('Veri')
plt.ylabel('Frekans')
plt.title('Verilerin Frekansları Histogramı')
plt.show()
