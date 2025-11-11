from django.urls import path
from . import views
urlpatterns = [
    path('usuarios/', views.UsuarioList.as_view(), name='usuario-list'),
    path('usuarios/<int:pk>/', views.UsuarioDetail.as_view(),name='usuario-detail'),
    path('produtos/', views.ProdutoList.as_view(), name='produto-list'),
    path('produtos/<int:pk>/', views.ProdutoDetail.as_view(),name='produto-detail'),
    path('servidor/', views.ServidorList.as_view(), name='servidor-list'),
    path('servidor/<int:pk>/', views.ServidorDetail.as_view(),name='servidor-detail'),
    path('pedidos/', views.PedidoList.as_view(), name='pedido-list'),
    path('pedidos/<int:pk>/', views.PedidoDetail.as_view(),name='pedido-detail'),
    path('imagens/', views.ImagemList.as_view(), name='imagem-list'),
    path('imagens/<int:pk>/', views.ImagemDetail.as_view(),name='imagem-detail'),
]