import pandas as pd
data= [514, 476, 497, 511, 484, 513, 471, 470, 441, 466, 443, 481, 502, 528, 459, 548, 521, 517,
463, 478, 473, 514, 542, 519, 522, 523, 546, 487, 486, 473, 527, 470, 440, 564, 499, 523,
484, 463, 461, 437, 555, 525, 461, 539, 466, 470, 486, 490, 543, 519]
x = pd.Series(data)
sonuc = pd.cut(x, bins=[436,452,468,484,500,516,532,548,564])
df = sonuc.value_counts().sort_index()
print("percent frequency table\n","Maaş aralıkları", "Yüzdeler")
print(100*(df / len(data)))
