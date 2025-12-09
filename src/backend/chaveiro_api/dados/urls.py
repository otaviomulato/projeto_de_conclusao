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
    # Rota do Site (HTML)
    path('catalog/', views.CatalogView.as_view(), name='catalog'),
    
    # Rotas da API (JSON)
    path('', include(router.urls)),
]