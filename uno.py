import serial
import os
from message_window import *
TARGET = serial.Serial("/dev/ttyUSB0", 9600)
last_value = 0
counter = 0
temperature_list = []

while True:
    temp = str(TARGET.readline())
    size = len(temp)-5
    temp = temp[2:size]
    temp = float(temp)
    if last_value != temp:
        temperature_list.append(temp)
        print(temp)
        counter += 1

    if counter == 6:
        break

    last_value = temp

os.system('clear')
suma = 0
size_list = 0
for i in temperature_list:
    suma += i
    size_list += 1

result = str(suma/size_list)
application = App(result)
