from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about-us/', views.about_us, name='about_us'),
    path('produtos/', views.produtos, name='produtos'),
    path('profile/', views.profile, name='profile'),
    path('sign-in/', views.sign_in, name='sign_in'),
    path('orders/', views.orders, name='orders'),
    path('testing-ground/', views.testing_ground, name='testing_ground'),
    path('forgot-password/', views.forgot_password_email, name='forgot_password_email'),
    path('forgot-password/code/', views.forgot_password_code, name='forgot_password_code'),
    path('redefine-password/', views.redefine_password, name='redefine_password'),
]
