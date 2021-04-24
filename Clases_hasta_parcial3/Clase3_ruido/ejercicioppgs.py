import pandas
import matplotlib.pyplot as plt
import  math

df = pandas.read_csv('/Users/danielzarate/Desktop/PDI/PDI-1/Clase3_ruido/PPG1.csv')
print(df)
print(df.columns)
df.plot( y = df.columns, kind = 'line', subplots = True)
plt.show()

from my_snr.py import my_snr
signal = df['Anular filtered']
noise = df['Anular'] - signal
snr_out = my_snr(signal, noise)
print('SNR is', snr_out)