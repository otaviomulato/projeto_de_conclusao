from django.shortcuts import render
from rest_framework import viewsets
from django.views.generic import ListView
from .models import Produto, Servidor, Pedido, Imagem, Usuario
from .serializers import ProdutoSerializer, ServidorSerializer, PedidoSerializer, ImagemSerializer, UsuarioSerializer
# Se 'cart' estiver dando erro, comente a linha abaixo temporariamente
# from cart.cart import Cart 

def index(request):
    return render(request, 'index.html')

# --- SUAS VIEWS DE API (Mantidas) ---
class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class ServidorViewSet(viewsets.ModelViewSet):
    queryset = Servidor.objects.all()
    serializer_class = ServidorSerializer

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

class ImagemViewSet(viewsets.ModelViewSet):
    queryset = Imagem.objects.all()
    serializer_class = ImagemSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

# --- VIEW DO SITE (Corrigida) ---
class CatalogView(ListView):
    model = Produto
    template_name = 'catalog.html'
    context_object_name = 'produtos' # Para facilitar no HTML
    paginate_by = 6
    queryset = Produto.objects.all()
    
    # Importante: NÃO adicione get_queryset com filtros se os campos não existem no banco.
    # O padrão já é pegar tudo (Produto.objects.all())

from django.shortcuts import render
from rest_framework import viewsets
from django.views.generic import ListView
from .models import Produto, Servidor, Pedido, Imagem, Usuario
from .serializers import ProdutoSerializer, ServidorSerializer, PedidoSerializer, ImagemSerializer, UsuarioSerializer

# --- VIEW DA PÁGINA INICIAL ---
def index(request):
    return render(request, 'index.html')

# --- VIEWS DA API (DRF) ---
class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class ServidorViewSet(viewsets.ModelViewSet):
    queryset = Servidor.objects.all()
    serializer_class = ServidorSerializer

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

class ImagemViewSet(viewsets.ModelViewSet):
    queryset = Imagem.objects.all()
    serializer_class = ImagemSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

# --- VIEWS DO SITE (HTML) ---

# 1. Catálogo (Classe - Para a listagem de produtos)
class CatalogView(ListView):
    model = Produto
    template_name = 'catalog.html'
    context_object_name = 'produtos'
    paginate_by = 6
    queryset = Produto.objects.all()

# 2. Outras Páginas (Funções - Para corrigir o erro de 'attribute missing')

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
    return render(request, 'forgot_password-code.html')

def redefine_password(request):
    return render(request, 'redefine-password.html')