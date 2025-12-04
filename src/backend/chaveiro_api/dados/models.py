from django.db import models
from usuarios.models import Usuario

# Create your models here.

class Produto(models.Model):
    nome_produto = models.CharField(max_length=50)
    descricao = models.TextField(blank=True, null=True)
    material = models.CharField(max_length=50)
    dimensoes = models.CharField(max_length=50)
    cor = models.CharField(max_length=50)
    preco = models.IntegerField()
    tipo_persona = models.CharField(max_length=50)
    link3D = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.nome_produto
class Servidor(models.Model):
    #nome_adm = models.CharField(max_length=50)
    #senha_adm = models.CharField(max_length=50)
    #email_adm = models.EmailField(max_length=100)
    ligado = models.BooleanField()
    credito_add = models.IntegerField()
    #FK_user_adm = models.ForeignKey(Usuario, related_name='dados',on_delete=models.CASCADE)

    def __str__(self):
        return self.credito_add
class Pedido(models.Model):
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_entrega = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField()
    persona = models.TextField(blank=True, null=True)
    avaliacao = models.TextField(blank=True, null=True)
    estrelas = models.IntegerField(blank=True, null=True)
    FK_user = models.ForeignKey(Usuario, related_name='dados',on_delete=models.CASCADE)
    FK_produto = models.ForeignKey(Produto, related_name='dados_pedi',on_delete=models.CASCADE)
    def __str__(self):
        return self.data_criacao
class Imagem(models.Model):
    img_produto = models.ImageField(upload_to='produtos/', blank=True, null=True)
    FK_produto = models.ForeignKey(Produto, related_name='dados_img',on_delete=models.CASCADE)
    def __str__(self):
        return f"Image for {self.smt.name}"