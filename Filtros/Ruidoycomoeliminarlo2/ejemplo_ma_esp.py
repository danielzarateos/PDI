
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

df = pd.read_csv('/Users/danielzarate/Desktop/PDI/PDI-1/Ruidoycomoeliminarlo/ecg_noisy.csv')
ecg1 = df['ECG1000']
ecg1 = ecg1 - np.mean(ecg1)
N = len(ecg1)
fs = 1000

plt.subplot(2,2,1)
plt.plot(ecg1)
window = np.ones(15)/15
ecg_avg = np.convolve(ecg1, window, mode='same')
#ecg_avg = np.convolve(ecg1, window)
#window = 30
#ecg_avg = np.zeros(N)
#for i in range(N-window):
#    ecg_avg[i+window] = np.mean(ecg1[i:i+window])

plt.subplot(2,2,3)
plt.plot(ecg_avg)

plt.subplot(2,2,2)
X1 = np.fft.fft(ecg1)
X1 = np.abs(X1)
f1 = (fs)*(np.arange(1,N+1)/N)
plt.plot(f1,X1)
plt.xlim((0, fs/2))

#FFT WINDOW
Xw = np.fft.fft(window, N)
Xw = np.abs(Xw)
fw = (fs)*(np.arange(1,N+1)/N)
#plt.plot(fw,Xw)
#plt.xlim((0, fs/2))



plt.subplot(2,2,4)
X2 = np.fft.fft(ecg_avg)
X2 = np.abs(X2)
N2 =len(ecg_avg)
f2 = (fs)*(np.arange(1,N2+1)/N2)
plt.plot(f2,X2)
plt.plot(fw,Xw)
plt.xlim((0, fs/2))
plt.show()
