from rest_framework import serializers
from .models import Store
from cnab.serializers import CnabSerializer
import ipdb

class StoreSerializer(serializers.ModelSerializer):
    balance = serializers.SerializerMethodField()
    operations = CnabSerializer(many=True)

    def get_balance(self, obj):
        balance = 0

        for operation in obj.operations.all():
            if operation.type == "entrance":
                balance += operation.value
            else:
                balance -= operation.value

        return balance
    
    class Meta:
        model = Store
        fields = ['id', 'name', 'balance', 'operations']