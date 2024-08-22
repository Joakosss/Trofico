import serial, time

arduino = serial.Serial('COM1', 9600)

while True:
    time.sleep(5)
    rawString = arduino.readline()
    print(rawString)
arduino.close()