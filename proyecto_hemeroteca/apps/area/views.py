from django.shortcuts import render

# REST IMPORTS
from rest_framework import viewsets

#APP IMPORTS
from .serializers import AreaSerializer
from .models import Area

# Create your views here.
class AreaViewSet(viewsets.ModelViewSet):
    serializer_class = AreaSerializer
    queryset = Area.objects.all()