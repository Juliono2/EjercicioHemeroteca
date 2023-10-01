from django.shortcuts import render
from django.http import HttpResponse

#REST Importrs
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets

#APP IMPORTS
from .serializers import LibroSerializer
from .models import Libro

# Create your views here.
def LibrosIndex(request):
    _Libro = Libro.objects.all()
    return HttpResponse(f"<h1>Hola desde view libros</h1><br>{_Libro[0].nombre}")

class LibrosApiView(APIView):
    def get(self, request, *args, **kwargs):

        _Libro = Libro.objects.all()

        data_response = [{"Titulo": Libro.titulo, "Tipo":Libro.tipo} for Libro in _Libro]

        return Response(data_response)
    
    def post(self, request, *args, **kwargs):
        data = request.data
        _Libro = Libro(tipo = data.get("tipo"),
                       titulo = data.get("titulo"),
                       fecha = data.get("fecha"),
                       editorial = data.get("editorial"))
        _Libro.save()

        return Response({"message": "Libro Creado"})
    
class LibroViewSet(viewsets.ModelViewSet):
    serializer_class = LibroSerializer
    queryset = Libro.objects.all()