import csv
import sys
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

x = []
y = []
z = []
roll = []
pitch = []
yawn = []
num_rows = 0

#data = [x y z roll pitch yawn]

# read data from .csv file
with open(sys.argv[1],'r') as csvfile:
	plots = csv.reader(csvfile, delimiter=',')
	for row in plots:
            print row
	    if row[0] != 'nan':
	    	x.append(float(row[0]))
	    if row[1] != 'nan':
	    	y.append(float(row[1]))
	    if row[2] != 'nan':
    		z.append(float(row[1]))
	    if row[3] != 'nan':
	    	roll.append(float(row[1]))
	    if row[4] != 'nan':
	    	pitch.append(float(row[1]))
	    if row[5] != 'nan':
	    	yawn.append(float(row[1]))

            num_rows = num_rows + 1


print("Accel_x mean: ", np.mean(x))
print("Accel_x var: ", np.var(x))

# Some constants from measurements
fs = 1000 # sample rate
ns = num_rows
T_beo = fs * ns # Beobachtungsdauer
f_res = float(fs)/ns

# Analyze x-accelaration
rfft_x = np.fft.rfft(x)
rfft_x = abs(rfft_x)/(len(rfft_x)/2)
fx_axis = f_res*np.arange(0,len(rfft_x))
fx_lds, Pxx_den = signal.periodogram(x, fs)

# Analyze y-accelaration
rfft_y = np.fft.rfft(y)
rfft_y = abs(rfft_y)/(len(rfft_y)/2)
fy_axis = f_res*np.arange(0,len(rfft_y))
fy_lds, Pyy_den = signal.periodogram(y, fs)

# Analyze z-accelaration
rfft_z = np.fft.rfft(z)
rfft_z = abs(rfft_z)/(len(rfft_z)/2)
fz_axis = f_res*np.arange(0,len(rfft_z))
fz_lds, Pzz_den = signal.periodogram(z, fs)

#create plot x-accelaration
plt.figure(1)
plt.subplot(311)
plt.title('IMU Values')
plt.plot(x) 
plt.xlabel('time')
plt.ylabel('Accel')
plt.subplot(312)
plt.title('FFT')
plt.plot(fx_axis, rfft_x)
plt.xlabel('frequency')
plt.ylabel('A')
plt.subplot(313)
plt.plot(fx_lds, Pxx_den)
plt.title('spectral density')
plt.xlabel('freq')
plt.ylabel('PSD')
plt.tight_layout()
#plt.show()

#create plot y-accelaration
plt.figure(2)
plt.subplot(311)
plt.title('IMU Values')
plt.plot(y) 
plt.xlabel('time')
plt.ylabel('Accel')
plt.subplot(312)
plt.title('FFT')
plt.plot(fy_axis, rfft_y)
plt.xlabel('frequency')
plt.ylabel('A')
plt.subplot(313)
plt.plot(fy_lds, Pyy_den)
plt.title('spectral density')
plt.xlabel('freq')
plt.ylabel('PSD')
plt.tight_layout()
#plt.show()

#create plot z-accelaration
plt.figure(3)
plt.subplot(311)
plt.title('IMU Values')
plt.plot(z) 
plt.xlabel('time')
plt.ylabel('Accel')
plt.subplot(312)
plt.title('FFT')
plt.plot(fz_axis, rfft_z)
plt.xlabel('frequency')
plt.ylabel('A')
plt.subplot(313)
plt.plot(fz_lds, Pzz_den)
plt.title('spectral density')
plt.xlabel('freq')
plt.ylabel('PSD')
plt.tight_layout()
plt.show()
