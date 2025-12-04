from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Cria um roteador e registra os ViewSets automaticamente
router = DefaultRouter()
router.register(r'produtos', views.ProdutoViewSet)
router.register(r'servidores', views.ServidorViewSet)
router.register(r'pedidos', views.PedidoViewSet)
router.register(r'imagens', views.ImagemViewSet)
router.register(r'usuarios', views.UsuarioViewSet)

urlpatterns = [
    # As URLs da API são geradas automaticamente aqui
    path('', include(router.urls)),
]