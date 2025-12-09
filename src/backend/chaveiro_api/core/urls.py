from django.urls import path
from dados import views 

urlpatterns = [
    # Página Inicial
    path('', views.index, name='index'),

    # Catálogo (Essa é a CLASSE que arrumamos)
    path('catalog/', views.CatalogView.as_view(), name='catalogo'),

    # Outras Páginas (Essas são as FUNÇÕES que adicionei agora)
    path('about-us/', views.about_us, name='about_us'),
    path('produtos/', views.produtos, name='produtos'),
    path('profile/', views.profile, name='profile'),
    path('sign-in/', views.sign_in, name='sign_in'),
    path('orders/', views.orders, name='orders'),
    path('testing-ground/', views.testing_ground, name='testing_ground'),
    
    # Recuperação de Senha
    path('forgot-password/', views.forgot_password_email, name='forgot_password_email'),
    path('forgot-password/code/', views.forgot_password_code, name='forgot_password_code'),
    path('redefine-password/', views.redefine_password, name='redefine_password'),
]