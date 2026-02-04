from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Usuario, Imovel, Contrato, Pagamento
from rest_framework.decorators import api_view
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
    
    ## GET Y POST ##
class UsuarioListCreateAPIView(ListCreateAPIView):
        queryset = Usuario.objects.all() #toma todos os objetos de la tabla de usuario
        serializer_class = UsuarioSerializer #Serializa los datos del usuario
        #devuelve los datos serializados
    
    
    ## GET e POST ##
@api_view(['GET', 'POST'])
def listar_usuarios(request):

    if request.method == 'GET':
        queryset = Usuario.objects.all()
        serializer = UsuarioSerializer(queryset, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UsuarioSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    ## UPDATE Y DELETE ##
class UsuarioUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    
    

## IMOVEL ##
class ImovelListCreateAPIView(ListCreateAPIView):
    queryset = Imovel.objects.all()
    serializer_class = ImovelSerializer
    

class ImovelUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Imovel.objects.all()
    serializer_class = ImovelSerializer
    
    
## CONTRATO ##
class ContratoListCreateAPIView(ListCreateAPIView):
    queryset = Contrato.objects.all()
    serializer_class = ContratoSerializer
    

class ContratoUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Contrato.objects.all()
    serializer_class = ContratoSerializer
    
    
 ## PAGAMENTO ##
class PagamentoListCreateAPIView(ListCreateAPIView):
    queryset = Pagamento.objects.all()
    serializer_class = PagamentoSerializer
    

class PagamentoUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Pagamento.objects.all()
    serializer_class = PagamentoSerializer