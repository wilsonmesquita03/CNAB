from rest_framework import serializers
from .models import Cnab

class CnabSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Cnab
        fields = ['id', 'type', 'data', 'value', 'cpf', 'card', 'store']

        