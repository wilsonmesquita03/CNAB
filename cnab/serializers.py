from rest_framework import serializers
from .models import Cnab

class CnabSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Cnab
        fields = ['id', 'type', 'date', 'value', 'cpf', 'card', 'store', 'nature', 'hour']
        read_only_fields = ['id', 'store']
        depth = 2

        