from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    # Página principal do carrinho (HTML)
    path('', views.cart_detail, name='cart_detail'),
    
    # Endpoints da API (usados pelo JavaScript)
    path('api/', views.cart_detail_api, name='cart_detail_api'),
    path('api/add/<int:product_id>/', views.cart_add_api, name='cart_add_api'),
    
    # Funcionalidades de atualização e remoção
    path('update/', views.cart_update, name='cart_update'),
    path('remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
]