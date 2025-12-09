# ... (mantenha seus imports e as classes ViewSet e CatalogView que já funcionam) ...

# --- FUNÇÕES DAS PÁGINAS (Adicione isso para as URLs funcionarem) ---

def about_us(request):
    return render(request, 'about_us.html')

def produtos(request):
    # Atenção: Se você quiser usar a mesma lógica do catálogo aqui, 
    # teremos que ajustar depois. Por enquanto, renderiza o HTML simples.
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
    return render(request, 'forgot_password-email.html') # Verifique se o nome do arquivo é esse mesmo

def forgot_password_code(request):
    return render(request, 'forgot_password-code.html')

def redefine_password(request):
    return render(request, 'redefine-password.html')
