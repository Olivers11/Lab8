import serial
from alert_window import * 
TARGET = serial.Serial("/dev/ttyUSB0", 9600)
initial_value = 0
last_status = 0
cont = 0

while True:
    temp = str(TARGET.readline())
    size = len(temp)-8
    temp = temp[2:size]
    num = int(temp)
    print(num)
    print(f"initial_value: {num}")
    if cont != 0:
        if num != last_status:
            if (num >= initial_value + 2) or num <= initial_value - 2 and cont >5:
                show_message()
            


    if cont == 1:
        initial_value = num

    cont += 1
    last_status = num



