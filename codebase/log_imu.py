import serial
import sys
import csv
import time

# needs the following parameter: devicepath / baudrate / log-time / (opt) output-filename
ser_path = ''
ser_rate = 0
log_time = 0
try:
    ser_path = sys.argv[1]
    ser_rate = sys.argv[2]
    log_time = sys.argv[3]
except: 
    print("Error processing arguments list.")
    print("PLease pass the following arguments: python log_imu.py <device_path> <baud_rate> <log_time(in s)> (opt)<output_file>")

# setup serial
ser = serial.Serial(ser_path, ser_rate, timeout=1)
ser.flushInput()

# start logging data
start = time.time()
while time.time() < start + log_time:
    try:
        ser_bytes = ser.readline()
        data = ser_bytes.split(',')

	with open("imu_log.csv", 'a') as f:
            writer = csv.writer(f, delimiter=",")
            n = [float('nan'), float('nan'), float('nan')], float('nan'), float('nan'), float('nan')]
	    for i in range(0,6):
                try:
                    n[i] = float(data[i])
		except:
		    print("wrong format!")
                    break
            writer.writerow(n)
    except:
        print("interrupted")
	break

print("Finished! Data wrote to csv-file.")
