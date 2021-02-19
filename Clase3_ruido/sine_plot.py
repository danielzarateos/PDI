import matplotlib.pyplot as plt
import numpy as np

# Dummy sine plot

#a = [0, np.pi/2, np.pi, np.pi*(3/2), np.pi*2]
#plt.plot(np.sin(a))
#plt.grid()
#plt.show()


# Neat sine plot

fs = 1000  # Sampling rate in Hz
start = 0  # initial time in seconds
stop = 3  # final time in seconds
f = 5  # Waverform frequency in Hz

# Create a list of evenly-spaced numbers over the range
t = np.linspace(start, stop, (stop-start)*fs)
y = np.sin(2*np.pi*t*f)
# Plot t vs y
plt.plot(t, y)       
plt.grid()
plt.show()

