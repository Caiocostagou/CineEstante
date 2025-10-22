# filmes/urls.py
from django.urls import path
from . import views

app_name = 'filmes'

urlpatterns = [
    # URLs antigas (mantidas)
    path('lista/', views.lista_filmes, name='lista'),
    path('buscar/', views.buscar_filmes, name='buscar'),
    
    # URLs novas - Sistema de Filmes
    path('filme/<int:filme_id>/', views.filme_detalhes, name='filme_detalhes'),
    path('filme/<int:filme_id>/adicionar/', views.adicionar_filme_estante, name='adicionar_filme_estante'),
    path('filme/<int:filme_id>/remover/', views.remover_filme_estante, name='remover_filme_estante'),
    
    # URLs novas - Sistema de Comentários
    path('filme/<int:filme_id>/comentar/', views.adicionar_comentario, name='adicionar_comentario'),
    path('comentario/<int:comentario_id>/curtir/', views.curtir_comentario, name='curtir_comentario'),
    path('comentario/<int:comentario_id>/deletar/', views.deletar_comentario, name='deletar_comentario'),
]