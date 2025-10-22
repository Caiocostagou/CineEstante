# usuarios/urls.py

from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    # Rota antiga (comentada - não está sendo usada)
    # path('perfil/', views.detalhe_perfil, name='perfil'),
    
    # Novas rotas
    path('editar-perfil/', views.editar_perfil, name='editar_perfil'),
    path('login/', views.login_view, name='login'),
    path('cadastro/', views.cadastro_view, name='cadastro'),
    path('logout/', views.logout_view, name='logout'),
    path('recuperar-senha/', views.recuperar_senha_view, name='recuperar_senha'),
]