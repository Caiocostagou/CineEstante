# usuarios/models.py

from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    """Perfil estendido do usuário"""
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    foto = models.ImageField(upload_to='perfis/', blank=True, null=True)
    bio = models.TextField(max_length=200, blank=True)
    localizacao = models.CharField(max_length=100, blank=True)
    filme_favorito = models.CharField(max_length=200, blank=True)
    perfil_publico = models.BooleanField(default=True)
    mostrar_estante = models.BooleanField(default=True)
    notificacoes = models.BooleanField(default=False)
    
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Perfil de {self.usuario.username}"
    
    def get_foto_url(self):
        """Retorna URL da foto ou avatar padrão"""
        if self.foto:
            return self.foto.url
        return f"https://ui-avatars.com/api/?name={self.usuario.get_full_name() or self.usuario.username}&background=8b5cf6&color=fff&size=256"
    
    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfis"

# FIM DO ARQUIVO - NÃO COLE MAIS NADA AQUI