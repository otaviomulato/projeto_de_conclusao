from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
    path('update/', views.cart_update, name='cart_update'),
    # API endpoints
    path('api/', views.cart_detail_api, name='cart_detail_api'),
    path('api/add/<int:product_id>/', views.cart_add_api, name='cart_add_api'),
]