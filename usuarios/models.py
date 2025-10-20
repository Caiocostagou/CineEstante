# usuarios/models.py

from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    # Cria uma relação um-para-um com o modelo de Usuário padrão do Django
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # Nossos campos personalizados
    descricao = models.TextField(blank=True)
    foto_perfil = models.ImageField(upload_to='fotos_perfil/', null=True, blank=True)

    def __str__(self):
        return self.usuario.username