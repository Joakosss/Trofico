from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http.response import JsonResponse
from . models import planta, registro, r_ambiente
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login as login_autent
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from .serializer import registroSerializer
import serial
# Create your views here.


def get_grafico(request):
    registros = registro.objects.all().order_by('-fecha')[:7]
    datos = {
        'labels': ["Ultimas mediciones"," "," "," "," "," "," "],
        'datasets': [{
            'label': 'Humedad',
            'data': [reg.humedad for reg in registros],
            'borderColor': 'rgba(75, 192, 192, 1)',
            'fill': False
        }]
    }
    return JsonResponse(datos)

    


class registroViewSet(viewsets.ModelViewSet):
    queryset = r_ambiente.objects.all()
    serializer_class = registroSerializer

@login_required(login_url='/login')
def index(request):
    plantas=planta.objects.all()

    registros = registro.objects.all().order_by('-fecha')[:6]

    registros = registro.objects.all()
    """ser = serial.Serial("COM4", 9600)
    datos = ser.readline().decode().strip()
    datos2 = round(100-((int(datos)/1024)*100))
    ser.close()

    # Guardar en la base de datos
    registro.objects.create(planta=planta.objects.get(id=15),
                            humedad=datos2)

    bool = False

    if int(datos)> 1000:
        bool = True
    """

    return render (request, 'index.html', {
        'plantas' : plantas,
        'registros' : registros,
        #'datos' : datos,
        #'datos2' : datos2,
        #'bool' : bool
    })

def logout_vista(request):
    logout(request)
    return redirect('LOGIN')


def login(request):
    if request.POST:
        usuario = request.POST.get("txtUsuario")
        clave = request.POST.get("txtClave")

        us= authenticate(request,username=usuario,password=clave)

        if us is not None and us.is_active:
                login_autent(request,us)
                plantas=planta.objects.all()
                registros = registro.objects.all()
                return redirect('INDEX')
        else:
            return render(request, 'login.html', {'msg':'usuario/contraseña invalido'})
    return render(request, 'login.html')

@login_required(login_url='/login')
def añadirPlanta(request):

    if request.POST:
        valorMin = request.POST.get("numMin")
        valorMax = request.POST.get("numMax")
        nombre = request.POST.get("txtNombrePlanta")
        descripcion = request.POST.get("txtaDescripcion")
        ubicacion = request.POST.get("txtUbicacion")

        plantanueva = planta(
            valorMin    = valorMin,
            valorMax    = valorMax,
            nombre      = nombre,
            descripcion = descripcion,
            ubicacion   = ubicacion,
        )

        if plantanueva is not None:
            plantanueva.save()
            return redirect('INDEX')
        else :
            return render(request,'agregarPlanta.html')

    return render(request,'agregarPlanta.html')