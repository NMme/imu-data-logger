import serial
import numpy as np
import csv
import time
ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
ser.flushInput()
time_out = 2
start = time.time()
while time.time() < start + time_out:
	try:
		ser_bytes = ser.readline()
		data = ser_bytes.split(',')
		with open("imu_log.csv", 'a') as f:
			writer = csv.writer(f, delimiter=",")
			n = [float('nan'), float('nan')]# float('nan')] #, float('nan'), float('nan'), float('nan')]
			for i in range(0,2):
				try:
					n[i] = float(data[i])
				except:
					print("wrong format!")
					break
			
			writer.writerow(n)
		
	except:
		print("interrupted")
		break
