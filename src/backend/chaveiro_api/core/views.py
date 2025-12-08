from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about_us(request):
    return render(request, 'about_us.html')

def produtos(request):
    return render(request, 'produtos.html')

def profile(request):
    return render(request, 'profile.html')

def sign_in(request):
    return render(request, 'sign_in.html')

def orders(request):
    return render(request, 'orders.html')

def testing_ground(request):
    return render(request, 'testing_ground.html')

def forgot_password_email(request):
    return render(request, 'forgot_password-email.html')

def forgot_password_code(request):
    return render(request, 'forgot-password-code.html')

def redefine_password(request):
    return render(request, 'redefine-password.html')
