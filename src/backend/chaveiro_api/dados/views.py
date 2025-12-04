from django.shortcuts import render
from rest_framework import viewsets
from .models import Produto, Servidor, Pedido, Imagem
from usuarios.models import Usuario
from .serializers import ProdutoSerializer, ServidorSerializer, PedidoSerializer, ImagemSerializer, UsuarioSerializer
# CORREÇÃO: Importa do app 'cart', não da pasta atual
from cart.cart import Cart

def index(request):
    return render(request, 'index.html')

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