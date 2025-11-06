from rest_framework import serializers
from .models import Usuario, Produto , Administrador , Pedido
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'
class AdministradorSerializer(serializers.ModelSerializer):
    #FK_user_adm = UsuarioSerializer(read_only=True)
    #usuario_id = serializers.PrimaryKeyRelatedField(queryset=Usuario.objects, source='FK_user_adm', write_only=True)
    class Meta:
        model = Administrador
        fields = '__all__'
class PedidoSerializer(serializers.ModelSerializer):
    FK_user = UsuarioSerializer(read_only=True)
    usuario_id = serializers.PrimaryKeyRelatedField(queryset=Usuario.objects, source='FK_user', write_only=True)
    FK_produto = ProdutoSerializer(read_only=True)
    produto_id = serializers.PrimaryKeyRelatedField(queryset=Produto.objects, source='FK_produto', write_only=True)
    class Meta:
        model = Pedido
        fields = '__all__'