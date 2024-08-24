from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'lecturas', views.registroViewSet)

urlpatterns = [
    path('', (views.index), name='INDEX'),
    path('login',(views.login), name='LOGIN'),
    path('logout_vista',(views.logout_vista),name='LOGOUT'),
    path('agregar_planta',views.añadirPlanta, name='PLANTAS'),
    path('api/', include(router.urls))
]
