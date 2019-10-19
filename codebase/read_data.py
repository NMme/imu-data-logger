import csv
import sys

def read_csv_input( filename ):
    x = []
    y = []
    z = []
    roll = []
    pitch = []
    yawn = []
    time_vector = []
    num_rows = 0

    # read data from .csv file
    with open(filename,'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=',')
            for row in plots:
                print row
                if row[0] != 'nan':
                    time_vector.append(int(float(row[0])))
                if row[1] != 'nan':
                    x.append(float(row[1]))
                if row[2] != 'nan':
                    y.append(float(row[2]))
                if row[3] != 'nan':
                    z.append(float(row[3]))
                if row[4] != 'nan':
                    roll.append(float(row[4]))
                if row[5] != 'nan':
                    pitch.append(float(row[5]))
                if row[6] != 'nan':
                    yawn.append(float(row[6]))
                num_rows = num_rows + 1

    return (time_vector, x, y, z, roll, pitch, yawn)
