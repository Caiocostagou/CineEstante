# filmes/models.py
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# =====================================================
# MODEL: FILME
# =====================================================
class Filme(models.Model):
    """Modelo para armazenar informações dos filmes"""
    
    # IDs e identificadores
    tmdb_id = models.IntegerField(unique=True, null=True, blank=True, help_text="ID do filme no TMDB")
    
    # Informações básicas
    titulo = models.CharField(max_length=255)
    titulo_original = models.CharField(max_length=255, blank=True)
    sinopse = models.TextField(blank=True)
    
    # Detalhes técnicos
    ano = models.IntegerField()
    duracao = models.CharField(max_length=50, blank=True)  # Ex: "119 min"
    genero = models.CharField(max_length=100)
    diretor = models.CharField(max_length=255, blank=True)
    elenco = models.TextField(blank=True, help_text="Elenco principal separado por vírgulas")
    
    # Avaliação
    nota = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)
    
    # Imagens (URLs)
    poster = models.URLField(max_length=500)
    backdrop = models.URLField(max_length=500, blank=True)
    
    # Metadados
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-ano', 'titulo']
        verbose_name = 'Filme'
        verbose_name_plural = 'Filmes'
    
    def __str__(self):
        return f"{self.titulo} ({self.ano})"
    
    def get_nota_estrelas(self):
        """Retorna a nota em formato de estrelas (0-5)"""
        return round(self.nota / 2, 1)


# =====================================================
# MODEL: ESTANTE (Lista de Filmes do Usuário)
# =====================================================
class Estante(models.Model):
    """Modelo para a lista de filmes de cada usuário"""
    
    STATUS_CHOICES = [
        ('assistido', 'Assistido'),
        ('quero_assistir', 'Quero Assistir'),
        ('assistindo', 'Assistindo'),
    ]
    
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='estante')
    filme = models.ForeignKey(Filme, on_delete=models.CASCADE, related_name='em_estantes')
    
    # Status e avaliação pessoal
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='quero_assistir')
    nota_pessoal = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True, help_text="Nota de 0 a 10")
    
    # Datas
    data_adicionado = models.DateTimeField(auto_now_add=True)
    data_assistido = models.DateField(null=True, blank=True)
    
    class Meta:
        unique_together = ['usuario', 'filme']
        ordering = ['-data_adicionado']
        verbose_name = 'Item da Estante'
        verbose_name_plural = 'Itens da Estante'
    
    def __str__(self):
        return f"{self.usuario.username} - {self.filme.titulo}"


# =====================================================
# MODEL: COMENTÁRIO
# =====================================================
class Comentario(models.Model):
    """Modelo para comentários dos usuários sobre filmes"""
    
    filme = models.ForeignKey(Filme, on_delete=models.CASCADE, related_name='comentarios')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comentarios')
    
    texto = models.TextField()
    
    # Metadados
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    editado = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-data_criacao']
        verbose_name = 'Comentário'
        verbose_name_plural = 'Comentários'
    
    def __str__(self):
        return f"{self.usuario.username} em {self.filme.titulo}"
    
    def total_curtidas(self):
        """Retorna o total de curtidas no comentário"""
        return self.reacoes.filter(tipo='curtida').count()
    
    def usuario_curtiu(self, usuario):
        """Verifica se o usuário curtiu este comentário"""
        return self.reacoes.filter(usuario=usuario, tipo='curtida').exists()


# =====================================================
# MODEL: REAÇÃO (Curtidas nos Comentários)
# =====================================================
class Reacao(models.Model):
    """Modelo para curtidas/reações em comentários"""
    
    TIPO_CHOICES = [
        ('curtida', '❤️ Curtida'),
    ]
    
    comentario = models.ForeignKey(Comentario, on_delete=models.CASCADE, related_name='reacoes')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reacoes')
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, default='curtida')
    
    data_criacao = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ['comentario', 'usuario']
        ordering = ['-data_criacao']
        verbose_name = 'Reação'
        verbose_name_plural = 'Reações'
    
    def __str__(self):
        return f"{self.usuario.username} {self.tipo} no comentário de {self.comentario.usuario.username}"