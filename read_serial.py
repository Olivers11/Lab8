import serial
TARGET = serial.Serial("/dev/ttyUSB0", 9600)


while True:
    temp = str(TARGET.readline())
    size = len(temp)-5
    print(temp[2:size])









