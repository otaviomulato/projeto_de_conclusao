from rest_framework import serializers
from .models import Usuario, Produto , Administrador
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'
class AdministradorSerializer(serializers.ModelSerializer):
    FK_user = UsuarioSerializer(read_only=True)
    usuario_id = serializers.PrimaryKeyRelatedField(queryset=Usuario.objects, source='FK_user', write_only=True)
    class Meta:
        model = Administrador
        fields = '__all__'