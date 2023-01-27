from rest_framework import serializers
from .models import Store
from cnab.serializers import CnabSerializer

class StoreSerializer(serializers.ModelSerializer):
    balance = serializers.SerializerMethodField()
    operations = CnabSerializer()

    def get_balance(self, obj):
        #write get balance code
        ...
    
    class Meta:
        model = Store
        fields = ['id', 'name', 'owner_name']