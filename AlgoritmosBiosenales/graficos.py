import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

df = pd.read_csv('outlier_ecg.csv')
ecg = df['ECG (500 Hz)']
# remuevo outliers
ecg = np.where(ecg > (np.mean(ecg) + 10*np.std(ecg)), np.mean(ecg), ecg)
ecg = np.where(ecg < (np.mean(ecg) - 10*np.std(ecg)), np.mean(ecg), ecg)
# normalizo
ecg = ecg - np.min(ecg)
ecg = ecg / np.max(ecg)
plt.plot(ecg)
plt.plot(168, 0.993, 'ro')
plt.plot(168, ecg[168], 'go')
plt.show()