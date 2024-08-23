from celery import shared_task
import serial
from .models import registro

def guardar_humedad():
    try:
        ser = serial.Serial("COM4", 9600)
        datos = ser.readline().decode().strip()
        ser.close()
        Humedad = round(100 - ((int(datos) / 1024) * 100))

        # Guardar en la base de datos
        registro.objects.create(planta=15,
                                humedad=Humedad)
    except Exception as e:
        # Manejo de errores
        print(f"Error: {e}")
