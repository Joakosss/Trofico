from rest_framework import serializers
from .models import r_ambiente

class registroSerializer(serializers.ModelSerializer):
    class Meta:
        model=r_ambiente
        #fields=('relativa','temperatura')
        fields = '__all__'