import serial
import requests
import json
from threading import Thread
from time import sleep

class SerialReader(Thread):
    def __init__(self, port, baudrate, api_url):
        super().__init__()
        self.port = port
        self.baudrate = baudrate
        self.api_url = api_url
        self.serial = serial.Serial(self.port, self.baudrate)
        self.running = True

    def run(self):
        while self.running:
            if self.serial.in_waiting > 0:
                line = self.serial.readline().decode('utf-8').strip()
                try:
                    data = json.loads(line)
                    response = requests.post(self.api_url, json=data)
                    print(f'Respuesta del servidor: {response.status_code} - {response.text}')
                except json.JSONDecodeError:
                    print("Error: Datos JSON no válidos")
            sleep(1)  # Pausa para no saturar la CPU

    def stop(self):
        self.running = False
        self.serial.close()
