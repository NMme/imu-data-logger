import csv
import sys
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

#x = []
x = []
y = []
z = []
num_rows = 0

with open(sys.argv[1],'r') as csvfile:
	plots = csv.reader(csvfile, delimiter=',')
	for row in plots:
		if row[0] != 'nan':
			x.append(float(row[0]))

		if row[1] != 'nan':
			z.append(float(row[1]))

                num_rows = num_rows + 1


#x = list(range(0, len(y))

#Do signal analyzing here
df = num_rows/2
fft_x = np.fft.fft(x)
fx, Pxx_den = signal.welch(x, df, nperseg=256)
#fx, t, Zxx = signal.stft(x, 1000, nperseg=200)

fft_z = np.fft.fft(z)
fz, Pzz_den = signal.welch(z, df, nperseg=256)

print("Accel_x mean: ", np.mean(x))
print("Accel_x var: ", np.var(x))

#create the plot
plt.figure(1, figsize=(18,10))
plt.subplot(311)
plt.title('IMU Values')
plt.plot(x) 
#plt.plot(y)
plt.plot(z)
plt.xlabel('time')
plt.ylabel('Accel')
#plt.subplot(312)
#plt.plot(fft_x)
#plt.plot(fft_y)
#plt.plot(fft_z)
#plt.title('FFT')
#plt.xlabel('freq')
#plt.ylabel('A')
plt.subplot(312)
#plt.pcolormesh(t, fx, np.abs(Zxx), vmin=0, vmax=3.5)
#plt.plot(fx, Pxx_den)
#plt.plot(fy, Pyy_den)
plt.plot(fz, Pzz_den)
plt.title('spectral density')
plt.xlabel('freq')
plt.ylabel('PSD')
plt.legend()
plt.show()

