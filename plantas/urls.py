from django.urls import path
from . import views



urlpatterns = [
    path('', (views.index), name='INDEX'),
    path('login',(views.login), name='LOGIN')
]
