from django.db import models

def get_imagem_principal(self):
    img = self.dados_img.first() # Pega a primeira imagem associada
    if img and img.img_produto:
        return img.img_produto.url
    return None

# Create your models here.
