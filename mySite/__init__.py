# myproject/__init__.py
from __future__ import absolute_import, unicode_literals

# Hacer que Celery cargue las tareas cuando Django arranca
from .celery import app as celery_app

__all__ = ('celery_app',)
