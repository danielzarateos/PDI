import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/danielzarate/Desktop/PDI/PDI-1/Lab1/data_example1.csv')
df.plot(x='Time', y = ['S1','S4'], kind = 'line')
#plt.show()

x = df['S1']
y = df['S4']

#Pearson's correlation coeff

N = len(x)
rxy = np.correlate(x-np.mean(x), y-np.mean(y))
#rxy = np.sum((x-np.mean(x))*(y-np.mean(y)))
prxy = rxy/(N-1)*np.sqrt((np.var(x)*np.var(y)))
plt.title('Pearson coeff  =' + str(np.round(prxy,2)))
print(np.corrcoef(x,y))
plt.show()

#SE NORMALIZA CON PEARSON

#MODE valid : derecho, same y full pueden desplazarse