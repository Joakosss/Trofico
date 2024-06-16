from django.contrib import admin
from .models import planta, registro
# Register your models here.

class plantaAdmin(admin.ModelAdmin):
    list_display=['id','valorMin','valorMax','nombre','descripcion','ubicacion']
    search_fields=['nombre','ubicacion','id']

class registroAdmin(admin.ModelAdmin):
    list_display=['id','planta','humedad','fecha']
    search_fields=['fecha','id']





admin.site.register(planta, plantaAdmin)
admin.site.register(registro, registroAdmin)

