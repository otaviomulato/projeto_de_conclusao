from rest_framework import serializers
from .models import Usuario, Produto , Servidor , Pedido , Imagem
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'
class ServidorSerializer(serializers.ModelSerializer):
    #FK_user_adm = UsuarioSerializer(read_only=True)
    #usuario_id = serializers.PrimaryKeyRelatedField(queryset=Usuario.objects, source='FK_user_adm', write_only=True)
    class Meta:
        model = Servidor
        fields = '__all__'
class PedidoSerializer(serializers.ModelSerializer):
    FK_user = UsuarioSerializer(read_only=True)
    usuario_id = serializers.PrimaryKeyRelatedField(queryset=Usuario.objects, source='FK_user', write_only=True)
    FK_produto = ProdutoSerializer(read_only=True)
    produto_id = serializers.PrimaryKeyRelatedField(queryset=Produto.objects, source='FK_produto', write_only=True)
    class Meta:
        model = Pedido
        fields = '__all__'
class ImagemSerializer(serializers.ModelSerializer):
    FK_produto = ProdutoSerializer(read_only=True)
    produto_id = serializers.PrimaryKeyRelatedField(queryset=Produto.objects, source='FK_produto', write_only=True)
    class Meta:
        model = Imagem
        fields = '__all__'