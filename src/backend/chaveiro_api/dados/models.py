from django.db import models

# Create your models here.
class Usuario(models.Model):
    nome_user = models.CharField(max_length=50)
    idade = models.PositiveIntegerField()
    profissao = models.CharField(max_length=50)
    credito = models.IntegerField()
    senha_user = models.CharField(max_length=50)
    email_user = models.EmailField(max_length=100)
    telefone = models.CharField(max_length=50)

    def __str__(self):
        return self.nome_user

class Produto(models.Model):
    nome_produto = models.CharField(max_length=50)
    descricao = models.TextField(blank=True)
    # imageNS no plural
    preco = models.IntegerField()
    tipo_persona = models.CharField(max_length=50)
    link3D = models.TextField(blank=True)

    def __str__(self):
        return self.nome_produto

class Administrador(models.Model):
    nome_adm = models.CharField(max_length=50)
    senha_adm = models.CharField(max_length=50)
    email_adm = models.EmailField(max_length=100)
    servidor = models.BooleanField()
    credito_add = models.IntegerField()
    #FK_user_adm = models.ForeignKey(Usuario, related_name='dados',on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_adm

class Pedido(models.Model):
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_entrega = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField()
    persona = models.TextField(blank=True)
    avaliacao = models.TextField()
    estrelas = models.IntegerField()
    FK_user = models.ForeignKey(Usuario, related_name='dados',on_delete=models.CASCADE)
    FK_produto = models.ForeignKey(Produto, related_name='dados',on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome_adm