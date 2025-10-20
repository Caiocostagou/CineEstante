# usuarios/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Perfil

@login_required # Garante que apenas usuários logados podem acessar esta página
def ver_perfil(request):
    # Busca o perfil do usuário logado. Se não existir, cria um novo.
    perfil, criado = Perfil.objects.get_or_create(usuario=request.user)

    if request.method == 'POST':
        # Se o formulário foi enviado, pega os dados
        perfil.descricao = request.POST.get('descricao')

        # Verifica se um novo arquivo de foto foi enviado
        if request.FILES.get('foto_perfil'):
            perfil.foto_perfil = request.FILES.get('foto_perfil')

        perfil.save() # Salva as alterações no banco de dados
        return redirect('ver_perfil') # Redireciona para a mesma página

    # Se não for um POST, apenas mostra a página
    return render(request, 'usuarios/perfil.html', {'perfil': perfil})