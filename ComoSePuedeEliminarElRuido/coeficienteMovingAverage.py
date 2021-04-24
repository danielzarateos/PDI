import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

df = pd.read_csv('/Users/danielzarate/Desktop/PDI/PDI-1/ComoSePuedeEliminarElRuido/ecg_noisy.csv')
ecg1 = df['ECG1000']
ecg1 = ecg1 - np.mean(ecg1)
N = len(ecg1)
fs = 1000

plt.subplot(2,2,1)
plt.plot(ecg1)
window = np.ones(15)/15
ecg_avg = np.convolve(ecg1, window)

plt.subplot(2,2,3)
plt.plot(ecg_avg)

plt.subplot(2,2,2)
X = np.fft.fft(ecg1)
X = np.abs(X)
f = (fs)*(np.arange(1,N+1)/N)
plt.plot(f,X)
plt.xlim((0, 200))
plt.title('Espectro ECG original')

# FFT de señal filtrada
N = len(ecg_avg)
plt.subplot(2,2,4)
Xf = np.fft.fft(ecg_avg)
Xf = np.abs(Xf)
f = (fs)*(np.arange(1,N+1)/N)
plt.plot(f,Xf)
plt.xlim((0, 200))
plt.title('Espectro ECG filtrado')

# FFT de window
Xw = np.fft.fft(window, N)
Xw = np.abs(Xw) 
plt.plot(f,Xw*np.max(X))
#plt.title('Espectro de coeficientes (b)')
plt.xlim((0, 200))

plt.show()