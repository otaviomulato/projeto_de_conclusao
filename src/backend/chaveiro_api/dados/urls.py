from django.urls import path
from . import views
urlpatterns = [
    path('usuarios/', views.UsuarioList.as_view(), name='usuario-list'),
    path('usuarios/<int:pk>/', views.UsuarioDetail.as_view(),name='usuario-detail'),
]