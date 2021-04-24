import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

df = pd.read_csv('ver.csv', header=None)
cols = df.columns
ver = df[cols[:]]
ver = ver.values

plt.subplot(2,1,1)
plt.plot(ver[:,5])
plt.title('Un solo potencial evocado')

ver_avg = np.mean(ver, axis=1)
plt.subplot(2,1,2)
plt.plot(ver_avg)
plt.title('El promedio de 100 potenciales evocados')
plt.show()
