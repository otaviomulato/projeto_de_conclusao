from django.urls import path
from . import views
urlpatterns = [
    path('usuarios/', views.UsuarioList.as_view(), name='usuario-list'),
    path('usuarios/<int:pk>/', views.UsuarioDetail.as_view(),name='usuario-detail'),
    path('produtos/', views.ProdutoList.as_view(), name='produto-list'),
    path('produtos/<int:pk>/', views.ProdutoDetail.as_view(),name='produto-detail'),
    path('adm/', views.AdministradorList.as_view(), name='administrador-list'),
    path('adm/<int:pk>/', views.AdministradorDetail.as_view(),name='administrador-detail'),
    path('pedidos/', views.PedidoList.as_view(), name='pedido-list'),
    path('pedidos/<int:pk>/', views.PedidoDetail.as_view(),name='pedido-detail'),
]