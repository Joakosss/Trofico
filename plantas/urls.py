from django.urls import path
from . import views



urlpatterns = [
    path('', (views.index), name='INDEX'),
    path('login',(views.login), name='LOGIN'),
    path('logout_vista',(views.logout_vista),name='LOGOUT'),
    path('agregar_planta',views.añadirPlanta, name='PLANTAS'),
]
