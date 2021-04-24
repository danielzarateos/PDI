import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import math 

df = pd.read_csv('eeg.csv')
print(df.head(5))

# Code here                     


# Plots
ax = plt.subplot(2,1,1)
plt.plot(f,X_mag)              
plt.xlabel('Frequency (Hz)',fontsize= 14)
plt.ylabel('|X(m)|',fontsize= 14)
ax = plt.subplot(2,1,2)
plt.plot(f,X_phase)              
plt.xlabel('Frequency (Hz)',fontsize= 14)
plt.ylabel('Phase (deg)',fontsize= 14)
plt.figure()
plt.plot(eeg)
plt.show()