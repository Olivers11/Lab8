import serial
import time
import csv

board = serial.Serial("/dev/ttyUSB0", 9600)

while True:

    temp = str(board.readline()) 
    size = len(temp)-8
    temp = temp[2:size]
    print(temp)
    with open("temperature_history.csv", "a") as f:
        writer = csv.writer(f, delimiter=",")
        writer.writerow([time.time(), temp])

