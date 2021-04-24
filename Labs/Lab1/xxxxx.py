from matplotlib import pyplot as plt
import serial
import numpy as np
import pandas as pd
 
Fs = 1000
t = 30   #10 segundos de grabación
signal = np.ones((Fs*t,1))
 
serial_com = '/dev/cu.usbmodem14101'  # seleccionar el COM adecuado
ser = serial.Serial(serial_com, baudrate = 115200, timeout=10)
 
 
for x in range(Fs*t):
        try:
            dat = int(ser.readline())
        except:
            dat = 0
        signal[x] = dat
        print(dat)
 
# Save the signal here as csv
df=pd.DataFrame(signal, columns=['Amplitude'])
df.to_csv('ECG_Elena.csv')
 
# Plot
plt.figure()
plt.plot(signal)
plt.show()
ser.close()