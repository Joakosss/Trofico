from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import planta, registro
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login as login_autent
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/login')
def index(request):
    plantas=planta.objects.all()
    registros = registro.objects.all()

    return render (request, 'index.html', {
        'plantas' : plantas,
        'registros' : registros
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