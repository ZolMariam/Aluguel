from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Usuario, Imovel, Contrato, Pagamento
from .serializer import (
    UsuarioSerializer,
    ImovelSerializer,
    ContratoSerializer,
    PagamentoSerializer
)

#class UsuarioListCreateAPIView(ListCreateAPIView):
    #def get(self, request):
       # usuarios = Usuario.objects.all() #toma todos os objetos de la tabla de usuario
        ##return Response(serializer.data) #devuelve los datos serializados
    
class UsuarioListCreateAPIView(ListCreateAPIView):
        queryset = Usuario.objects.all() #toma todos os objetos de la tabla de usuario
        serializer_class = UsuarioSerializer #Serializa los datos del usuario
 #devuelve los datos serializados