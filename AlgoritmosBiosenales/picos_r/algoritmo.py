import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
from scipy import signal

df = pd.read_csv('ecg1.csv')
ecg = df['ECG (500 Hz)']

# normalizo
ecg = ecg - np.min(ecg)
ecg = ecg / np.max(ecg)
# plt.plot(ecg)
# plt.show()

# Encuentro picos onda R
# threshold = 0.3
# aux = ecg > threshold
# aux = ecg*aux
# plt.plot(aux)
# plt.show()
# ind_peaks, _ = signal.find_peaks(aux)
ind_peaks, _ = signal.find_peaks(ecg, height= 0.3)
print(ind_peaks)
plt.plot(ecg)
plt.plot(ind_peaks, ecg[ind_peaks], 'ro')
plt.show()