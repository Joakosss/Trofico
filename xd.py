import serial, time
arduino = serial.Serial('COM4', 9600)
while True:
    time.sleep(180)
    rawString = arduino.readline()
    print(rawString)
arduino.close()j