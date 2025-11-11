from django.shortcuts import render
from rest_framework import generics
<<<<<<< HEAD
from .models import Usuario , Produto , Administrador , Pedido
from .serializers import UsuarioSerializer , ProdutoSerializer , AdministradorSerializer , PedidoSerializer

def home_view(request):
    return render(request, 'index.html')

def about_us(request):
    return render(request, 'about_us.html')





#serializers do usuario, produto e admin (por enquanto)
=======
from .models import Usuario , Produto , Servidor , Pedido , Imagem
from .serializers import UsuarioSerializer , ProdutoSerializer , ServidorSerializer , PedidoSerializer , ImagemSerializer

>>>>>>> f629aba7c3f2ea3f565ec497dca257ab70431404
class UsuarioList(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class UsuarioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class ProdutoList(generics.ListCreateAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class ProdutoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

<<<<<<< HEAD
class AdministradorList(generics.ListCreateAPIView):
    queryset = Administrador.objects.all()
    serializer_class = AdministradorSerializer

class AdministradorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Administrador.objects.all()
    serializer_class = AdministradorSerializer
=======
class ServidorList(generics.ListCreateAPIView):
    queryset = Servidor.objects.all()
    serializer_class = ServidorSerializer

class ServidorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Servidor.objects.all()
    serializer_class = ServidorSerializer
>>>>>>> f629aba7c3f2ea3f565ec497dca257ab70431404

class PedidoList(generics.ListCreateAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

class PedidoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

class ImagemList(generics.ListCreateAPIView):
    queryset = Imagem.objects.all()
    serializer_class = ImagemSerializer

class ImagemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Imagem.objects.all()
    serializer_class = ImagemSerializer