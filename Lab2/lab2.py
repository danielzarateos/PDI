#Importar
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
from statistics import mean

#Leer 

doc_peaks = pd.read_csv('/Users/danielzarate/Desktop/PDI/PDI-1/Lab2/ecg_1min_rpeaks.csv')
doc_min = pd.read_csv('/Users/danielzarate/Desktop/PDI/PDI-1/Lab2/ecg_1min.csv')
doc_signal = pd.read_csv('/Users/danielzarate/Desktop/PDI/PDI-1/Lab2/signal1.csv')
doc_signal_lista = doc_signal['Signal']
doc_min_lista = doc_min['ECG']
doc_peaks_lista = doc_peaks['R peaks']


#1. Construya la señal de diente de sierra que se muestra a continuación 
# y use la función fft para encontrar su espectro de frecuencia. 
# Luego, reconstruya la señal usando los primeros 24 componentes por dos vías
#  usando ifft y usando la ecuación

#Desarrollo
fs = 1024    #frecuencia de muestreo 
f1 = 1 / fs  #periodo de muestreo
Tt = 1       #total time           
N = Tt * fs  #numero de muestras       


signal_time = np.arange(0, Tt, f1)  
signal_organizada = np.zeros(N)

signal_organizada[0:N//2] = signal_time[0:N//2]
signal_organizada[N//2:N] = signal_time[0:N//2]

signal_organizada *= 2  #Para que vaya de 0 a 1
signal_organizada -= .5 #Para que baje

# FFT (reemplaza el ciclo for del ejemplo 1)
X= np.fft.fft(signal_organizada)
X = np.abs(X) #X es equivalente a X_mag

# Frequency vector
f = (fs)*(np.arange(1,N+1)/N)
plt.figure()
plt.plot(f,X)
plt.title('Vector de frecuencia señal generada',fontsize=14)
plt.show()

X= np.fft.fft(signal_organizada)

# Frequency vector (half!)
N2 = np.round(N/2)
f2 = (fs/2)*(np.arange(1,N2+1)/N2)
X2 = X[0:int(N2)]

#IFFT 

# Reconstruccion IFFT
aux_index = np.arange(24,N-23) #Coger de 0 a 23
X[aux_index] = 0 + 0j       #Apagar imaginarios
sig_r = np.fft.ifft(X)      #Tomo IFFT con las apagadas
sig_r = np.real(sig_r)

plt.figure()
plt.plot(signal_time,signal_organizada)
plt.plot(signal_time,sig_r, linestyle='dashed', color='blue')
plt.xlabel('Time(sec)',fontsize=14)
plt.ylabel('signal(t)',fontsize=14)
plt.title('24 Primeros puntos reconstruidos IFFT',fontsize=14)
plt.show()

# Descomposicion Fourier 
a0 = 2*np.mean(signal_organizada)
print(a0)
f = np.zeros(round(N/2))
X_mag = np.zeros(round(N/2)) 
X_phase = np.zeros(round(N/2))     
# Construct waveform 
for m in range(1,250):
    f[m] = m*f1
    a = (2/N)*np.sum(signal_organizada*(np.cos(2*np.pi*f[m]*signal_time)))
    b = (2/N)*np.sum(signal_organizada*(np.sin(2*np.pi*f[m]*signal_time)))
    X_mag[m] = np.sqrt((a**2) + (b**2))
    X_phase[m] = -math.atan2(b,a)
# Reconstruction
for m in range(1,24):
    sig_rE = sig_r + X_mag[m] * np.cos(2*np.pi*f[m]*signal_time + X_phase[m])
sig_rE = sig_r + a0/2

plt.figure()
plt.plot(signal_time,signal_organizada)
plt.plot(signal_time,sig_rE, linestyle='dashed', color='red')
plt.xlabel('Time(sec)',fontsize=14)
plt.ylabel('signal(t)',fontsize=14)
plt.title('24 Primeros puntos reconstruidos Fourier',fontsize=14)
plt.show()

#Realice el plot ambas señales (original y reconstruida) en la misma gráfica 
#para cada alternativa por separado. Para que ambas señales coincidan en escala, 
#recuerde normalizar el resultado encontrado con fft con N2 
#(es decir, dividirlo por ese valor). Defina fs = 1024 y N = 1024 
#para representar la señal periódica de 1s. 
# Recuerde además que el primer elemento del vector complejo producido 
# por la rutina fft es el componente DC.

#2. El archivo signal1.csv DOC_SIGNAL contiene una señal que consta de dos senoidales 
#(200 y 400 Hz) con un SNR de -12 dB. 
#La frecuencia de muestreo es de 1 KHz su tamaño es N=4096. 
#Realice los siguientes procedimientos:

#a. Grafique el espectro de frecuencia de la señal completa usando la función fft.

fs = 1000   
N = len(doc_signal_lista)
X = np.fft.fft(doc_signal_lista) #X es equivalente a X_mag
X = np.abs(X) #excluye los numeros imaginarios, toma solo la parte real              
f = (fs)*(np.arange(1,N+1)/N)  #Frecuencia por formula

plt.figure()
plt.plot(f,X)
plt.title('espectro Signal1.csv',fontsize=14)
plt.show()

#b. Grafique el espectro de frecuencia usando fft con porciones de menor tamaño a 
#partir de la señal original:

#De 1 a 2048 
N2 = np.round(N/2)
f2 = (fs*2)*(np.arange(1,N2+1)/N2)
X2 = X[0:int(N2)]
plt.figure()
plt.plot(f2,X2)
plt.title('Espectro de frecuencia Signal1.csv 1 a 2048',fontsize=14)
plt.show()
#De 1 a 1024 
N3 = np.round(N/4)
f3 = (fs)*(np.arange(1,N3+1)/N3)
X3 = X[0:int(N3)]
plt.figure()
plt.plot(f3,X3)
plt.title('Espectro de frecuencia Signal1.csv 1 a 1024',fontsize=14)
plt.show()
#De 1 a 512 
N4 = np.round(N/8)
f4 = (fs/2)*(np.arange(1,N4+1)/N4)
X4 = X[0:int(N4)]
plt.figure()
plt.plot(f4,X4)
plt.title('Espectro de frecuencia Signal1.csv 1 a 512',fontsize=14)
plt.show()
#De 1 a 256 
N5 = np.round(N/16)
f5 = (fs/5)*(np.arange(1,N5+1)/N5)
X5 = X[0:int(N5)]
plt.figure()
plt.plot(f5,X5)
plt.title('Espectro de frecuencia Signal1.csv 1 a 256',fontsize=14)
plt.show()
#De 1 a 128
N6 = np.round(N/32)
f6 = (fs/8)*(np.arange(1,N6+1)/N6)
X6 = X[0:int(N6)]
plt.figure()
plt.plot(f6,X6)
plt.title('Espectro de frecuencia Signal1.csv 1 a 128',fontsize=14)
plt.show()

#¿Qué cambia en el espectro?
#¿Por qué al cambiar el tamaño de la porción cambia la forma del espectro? 

#c. Realice el procedimiento anterior nuevamente,pero llene con zero padding cada porción 
#Analice el resultado y argumente el porqué de lo observado.

X7 = np.zeros(4096)
fs = 1000   
X7[0:int(N2)] = X[0:int(N2)]
X7 = np.abs(X7)
plt.figure()
plt.plot(f*4,X7)
plt.title('espectro Signal1 con zeros padding hasta 2048.csv',fontsize=14)
plt.show()


X8 = np.zeros(4096)
fs = 1000   
X8[0:int(N3)] = X[0:int(N3)]
X8 = np.abs(X8) 
plt.figure()
plt.plot(f*4,X8)
plt.title('espectro Signal1 con zeros padding hasta 1024.csv',fontsize=14)
plt.show()

X9 = np.zeros(4096)
fs = 1000   
X9[0:int(N4)] = X[0:int(N4)]
X9 = np.abs(X9)
plt.figure()
plt.plot(f*4,X9)
plt.title('espectro Signal1 con zeros padding hasta 512.csv',fontsize=14)
plt.show()

X10 = np.zeros(4096)
fs = 1000   
X10[0:int(N5)] = X[0:int(N5)]
X10 = np.abs(X10)
plt.figure()
plt.plot(f*4,X10)
plt.title('espectro Signal1 con zeros padding hasta 256.csv',fontsize=14)
plt.show()

X11 = np.zeros(4096)
fs = 1000   
X11[0:int(N6)] = X[0:int(N6)]
X11 = np.abs(X11)
plt.figure()
plt.plot(f*4,X11)
plt.title('espectro Signal1 con zeros padding hasta 128.csv',fontsize=14)
plt.show()
  
#3. El archivo ecg_1min.csv contiene 60 segundos de la electrocardiografía 
#de una persona muestreada a 250 Hz


#a. Grafique el espectro de frecuencia de la señal haciendo zoom en la región de 0 a 20 Hz. 
# Proponga una estrategia, basada en las variables del espectro (f y X_mag) para encontrar 
# la frecuencia cardiaca promedio de la persona durante esos 60 segundos. 
# Le puede ser de ayuda saber que normalmente la frecuencia cardiaca de una persona oscila en el 
# rango de 40 a 180 latidos por minuto. Su estrategia debe ser completamente automática,
#  es decir al final con un print(resultado) se debe poder ver la frecuencia cardiaca de la señal.


ecg_csv = pd.read_csv("/Users/danielzarate/Desktop/PDI/PDI-1/Lab2/ecg_1min.csv")
ecg_array = ecg_csv["ECG"]
fs_ecg = 250
periodo_fs_ecg = 1 / fs_ecg
divisor_ecg = fs_ecg / 20
N_ecg = len(ecg_array)
N_zoom = N_ecg // divisor_ecg
arreglo_fft = np.abs(np.fft.fft(ecg_array))
zoom_ecg_lista = arreglo_fft[0: int(N_zoom)]
f_lista = fs_ecg * (np.arange(N_ecg) / N_ecg)
f_zoom_lista = (fs_ecg / divisor_ecg)*(np.arange(N_zoom) / N_zoom)

plt.figure()
plt.plot(f_lista, arreglo_fft)
plt.title("Frecuencia")
plt.show()

plt.figure()
plt.plot(f_zoom_lista, zoom_ecg_lista)
plt.title("Con zoom")
plt.show()

plt.show()
posicion_frecuencia_max = np.argmax(arreglo_fft) #Valor maximo de mi arreglo
valor_frecuencia_mas_alto = f_lista[posicion_frecuencia_max] #Valor frecuencia mas similar
#Ahora si tomamos la frecuencia, la cual esta en Hz osea ciclos por segundo, 
# y la multiplicamos por 60s obtenemos 
#ciclos por minuto
ritmo_cardiaco = valor_frecuencia_mas_alto * 60
print("El ritmo cardiaco es de {}bpm".format(round(ritmo_cardiaco)))

        