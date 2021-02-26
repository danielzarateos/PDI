import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('data_example1.csv')
df.plot(x='Time', y = ['S1','S3'], kind = 'line')
#plt.show()

x = df['S1']
y = df['S4']

#Pearson's correlation coeff

N = len(x)
rxy = (x-np.mean(x))*(y-np.mean(y))
prxy = rxy/(N-1)*np.sqrt((np.var(x)*np.var(y)))
plt.title('Pearson coeff  =' + str(round(prxy,2)))
plt.show()