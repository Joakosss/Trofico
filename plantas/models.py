from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)


class planta (models.Model):
    valorMin =models.IntegerField()
    valorMax =models.IntegerField()
    nombre =models.CharField(max_length=50)
    descripcion = models.TextField(max_length=100)
    ubicacion = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.nombre
class registro (models.Model):
    planta =models.ForeignKey(planta, on_delete=models.CASCADE)
    humedad =models.IntegerField()
    fecha =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """ return self.planta.nombre """ 
        return self.fecha.strftime("%d/%m/%Y , %H:%M:%S"+ " " +self.planta.nombre)
    