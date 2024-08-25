from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http.response import JsonResponse
from . models import planta, registro
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login as login_autent
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from .serializer import registroSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import registro
import json, requests, serial

# Create your views here.
@api_view(['POST'])
def recibir_datos(request):
    try:
        data = json.loads(request.body)
        serializer = registroSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except json.JSONDecodeError:
        return Response({"error": "Datos JSON no válidos"}, status=status.HTTP_400_BAD_REQUEST)

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
    queryset = registro.objects.all()
    serializer_class = registroSerializer

def lectura_arduino():
    ser = serial.Serial('COM4', 9600)

    # URL del endpoint de API Django local
    url = 'http://127.0.0.1:8000/api/recibir_datos/'

    planta_id = 15
    humedad = 65
    c = 0

    while c < 1:
        line = ser.readline().decode('utf-8').strip()
        try:
            # Cargar los datos JSON recibidos
            data = json.loads(line)
            
            data['planta'] = planta_id
            data['humedad'] = humedad
            
            # Enviar los datos actualizados a la API
            response = requests.post(url, json=data)
            c += 1
            print(f'Respuesta del servidor: {response.status_code} - {response.text}')
        except json.JSONDecodeError:
            print("Error: Datos JSON no válidos")
        break

@login_required(login_url='/login')
def index(request):
    lectura_arduino()
    plantas=planta.objects.all()

    registros = registro.objects.all().order_by('-fecha')[:6]

    ultimo_registro = registro.objects.latest('fecha')

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
        'ultimo_registro' : ultimo_registro,
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