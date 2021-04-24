import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import math
import csv
from statistics import mean

npts = 2000
x = np.linspace(0, 50, npts)
doc_neural_data = pd.read_csv('/Users/danielzarate/Desktop/PDI/PDI-1/Parcial1/neural_data.csv')
lista_neuron1 = doc_neural_data['Neuron 1']
lista_neuron2 = doc_neural_data['Neuron 2']
doc_neural_data.plot()
plt.show()
x = doc_neural_data['Neuron 1']
y = doc_neural_data['Neuron 2']
#Pearson's correlation coeff
N = len(x)
rxy = np.correlate(x-np.mean(x), y-np.mean(y))
prxy = rxy/(N-1)*np.sqrt((np.var(x)*np.var(y)))
print('El coeficiente de pearson de estas dos señales es de ' + str(np.round(prxy,2)))
print("Aunque no me esta dando la correlacion bien, se puede ver que si estan asociadas a un mismo \n proceso ya que la señal Neuron 2 parece ser una replica o reaccion con cierto delay o offset \n (fisiologico) de la señal 1")
#2
doc_ecg = pd.read_csv('/Users/danielzarate/Desktop/PDI/PDI-1/Parcial1/ecg.csv')
doc_ecg_lista = doc_ecg['ECG']
doc_ecg_lista.plot()
plt.title('ECG completo')
plt.show()
fs = 1000   
N = len(doc_ecg_lista)
X = np.fft.fft(doc_ecg_lista) #X es equivalente a X_mag
X = np.abs(X) #excluye los numeros imaginarios, toma solo la parte real              
f = (fs/60000)*(np.arange(1,N+1)/N)  #Frecuencia por formula
plt.figure()
plt.plot(f,X)
plt.title('Espectro ECG.csv',fontsize=14)
plt.show()
f1 = 1/N    
t = np.arange(1,N+1)/fs 
# Reconstruction (ifft)
#aux_index = np.arange(0,1) #estoy apagando los valores desde la posicion 5 hasta la posición 196
#X[aux_index] = 0 + 0j #estamos apagando algunas frecuencias de la descomposición
sig_r = np.fft.ifft(X)
sig_r = np.real(sig_r)
plt.figure()
plt.plot(t,sig_r)
#plt.plot(t,doc_ecg_lista, linestyle='dashed')
plt.xlabel('Time(sec)',fontsize=14)
plt.ylabel('x(t)',fontsize=14)
plt.ylim(-1,1)
plt.title('Para hallar Frecuencia vemos que el seno hace un ciclo cada 2s ',fontsize=14)
print("La frecuencia del ruido es de 0.5 Hz porque en 1000 muestras tomadas a 1000Hz solo logra \n hacer medio ciclo")
plt.show()
# Reconstruction (ifft)
aux_index = np.arange(0,5) 
X[aux_index] = 0 + 0.5
sig_r = np.fft.ifft(X)
sig_r = np.real(sig_r)

plt.figure()
plt.plot(t,sig_r)
plt.xlabel('Time(sec)',fontsize=14)
plt.ylabel('x(t)',fontsize=14)
plt.title('Reconstruccion sin frecuencias de 0.5Hz (no quedo bien)',fontsize=14)
plt.show()


