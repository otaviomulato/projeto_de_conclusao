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