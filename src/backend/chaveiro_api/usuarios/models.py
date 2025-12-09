from django.db import models

class Usuario(models.Model):
    nome_user = models.CharField(max_length=50)
    idade = models.PositiveIntegerField()
    profissao = models.CharField(max_length=50)
    credito = models.IntegerField(default=0)
    senha_user = models.CharField(max_length=50)
    email_user = models.EmailField(max_length=100, unique=True)
    telefone = models.CharField(max_length=50)
    
    # Novo campo para "Soft Delete"
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nome_user