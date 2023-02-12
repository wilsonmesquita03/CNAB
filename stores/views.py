from django.shortcuts import render
from rest_framework import generics
from .serializers import StoreSerializer
from .models import Store

# Create your views here.

class StoreView(generics.ListAPIView):
    serializer_class = StoreSerializer
    queryset = Store.objects.all()

class StoreDetailedView(generics.RetrieveAPIView):
    serializer_class = StoreSerializer
    queryset = Store.objects.all()
    lookup_url_kwarg = "pk"
