from django.shortcuts import render
from rest_framework import generics
from .models import Usuario , Produto , Servidor , Pedido , Imagem
from .serializers import UsuarioSerializer , ProdutoSerializer , ServidorSerializer , PedidoSerializer , ImagemSerializer

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

class ServidorList(generics.ListCreateAPIView):
    queryset = Servidor.objects.all()
    serializer_class = ServidorSerializer

class ServidorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Servidor.objects.all()
    serializer_class = ServidorSerializer

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