from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    # APIs de Autenticação
    path('api/register/', views.register_api, name='register_api'),
    path('api/login/', views.login_api, name='login_api'),
    path('logout/', views.logout_view, name='logout'),

    # APIs de Perfil (O HTML consome isso aqui)
    path('api/profile/', views.profile_api, name='profile_api'),
    path('api/deactivate/', views.deactivate_account, name='deactivate_api'),
]