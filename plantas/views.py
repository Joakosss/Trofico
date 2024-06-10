from django.shortcuts import render
from django.http import HttpResponse
from . models import planta, registro

# Create your views here.
def about(request):
    return HttpResponse("xd")

def index(request):
    plantas=planta.objects.all()
    registros = registro.objects.all()

    return render (request, 'index.html', {
        'plantas' : plantas,
        'registros' : registros

    })
