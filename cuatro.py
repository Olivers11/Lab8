import serial
import time
import csv
from datetime import datetime

board = serial.Serial("/dev/ttyUSB0", 9600)
initial = datetime.now()
while True:

    temp = str(board.readline()) 
    size = len(temp)-8
    temp = temp[2:size]
    print(temp)
    with open("temperature_history2.csv", "a") as f:
        writer = csv.writer(f, delimiter=",")
        final = datetime.now()
        _time = final - initial
        minutes = _time.seconds/60
        writer.writerow([round(minutes,2), temp])

