from django.urls import path
from .views import UsuarioListCreateAPIView, UsuarioUpdateDestroyView, listar_usuarios, ContratoListCreateAPIView, ContratoUpdateDestroyView, ImovelListCreateAPIView, ImovelUpdateDestroyView, PagamentoListCreateAPIView, PagamentoUpdateDestroyView

urlpatterns = [
    path('usuarios/', UsuarioListCreateAPIView.as_view()),
    path('usuario/<int:pk>', UsuarioUpdateDestroyView.as_view()),
    path('users/', listar_usuarios),
    
    path('contratos/', ContratoListCreateAPIView.as_view()),
    path('contrato/<int:pk>', ContratoUpdateDestroyView.as_view()),
    
    path('imoveis/', ImovelListCreateAPIView.as_view()),
    path('imovel/<int:pk>', ImovelUpdateDestroyView.as_view()),
    
    path('pagamentos/', PagamentoListCreateAPIView.as_view()),
    path('pagamento/<int:pk>', PagamentoUpdateDestroyView.as_view()),
]
