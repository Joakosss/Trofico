# myproject/celery.py
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Configura el módulo de configuración para Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mySite.settings')

app = Celery('myproject')

# Usar la configuración de Django
app.config_from_object('django.conf:settings', namespace='CELERY')

# Cargar tareas de todos los módulos de tareas en el proyecto
app.autodiscover_tasks()

# myproject/celery.py
from celery.schedules import crontab

app.conf.beat_schedule = {
    'guardar-humedad-diariamente': {
        'task': 'plantas.tasks.guardar_humedad',
        #'schedule': crontab(hour=13, minute=0),  # Ejecutar a las 00:00 (medianoche)
        'schedule': crontab(minute='*/1'),  # Ejecutar cada minuto
    },
}