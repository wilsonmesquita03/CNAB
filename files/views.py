from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.parsers import FormParser
from .models import File
import ipdb

# Create your views here.
class CreateCnabView(APIView):
    parser_classes = [FormParser]
    
    def post(self, request, format=None):
        print(request.FILES)


