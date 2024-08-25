from rest_framework import serializers
from .models import registro

class registroSerializer(serializers.ModelSerializer):
    class Meta:
        model= registro
        #fields = ('planta', 'relativa', 'temperatura')
        fields= '__all__'