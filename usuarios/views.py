# usuarios/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Perfil

# ========== FUNÇÃO ANTIGA (mantém) ==========
def detalhe_perfil(request):
    return render(request, 'usuarios/perfil.html')


# ========== NOVAS FUNÇÕES (adiciona) ==========
def login_view(request):
    if request.user.is_authenticated:
        return redirect('filmes:lista')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f'Bem-vindo de volta, {user.first_name or user.username}!')
            next_page = request.GET.get('next', 'filmes:lista')
            return redirect(next_page)
        else:
            messages.error(request, 'Usuário ou senha incorretos!')
    
    return render(request, 'usuarios/login.html')


def cadastro_view(request):
    if request.user.is_authenticated:
        return redirect('filmes:lista')
    
    if request.method == 'POST':
        nome_completo = request.POST.get('nome_completo')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        
        if password != password2:
            messages.error(request, 'As senhas não coincidem!')
            return render(request, 'usuarios/cadastro.html')
        
        if len(password) < 8:
            messages.error(request, 'A senha deve ter no mínimo 8 caracteres!')
            return render(request, 'usuarios/cadastro.html')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Nome de usuário já existe!')
            return render(request, 'usuarios/cadastro.html')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'E-mail já cadastrado!')
            return render(request, 'usuarios/cadastro.html')
        
        try:
            nome_parts = nome_completo.split()
            first_name = nome_parts[0] if nome_parts else ''
            last_name = ' '.join(nome_parts[1:]) if len(nome_parts) > 1 else ''
            
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name
            )
            
            messages.success(request, 'Conta criada com sucesso! Faça login para continuar.')
            return redirect('usuarios:login')
            
        except Exception as e:
            messages.error(request, f'Erro ao criar conta: {str(e)}')
    
    return render(request, 'usuarios/cadastro.html')


@login_required
def logout_view(request):
    logout(request)
    messages.success(request, 'Você saiu da sua conta!')
    return redirect('usuarios:login')


def recuperar_senha_view(request):
    messages.info(request, 'Funcionalidade em desenvolvimento!')
    return redirect('usuarios:login')

@login_required
def editar_perfil(request):
    """View para editar perfil do usuário"""
    # Busca ou cria perfil do usuário
    perfil, created = Perfil.objects.get_or_create(usuario=request.user)
    
    if request.method == 'POST':
        # Dados pessoais
        nome_completo = request.POST.get('name', '')
        if nome_completo:
            partes = nome_completo.split()
            request.user.first_name = partes[0]
            request.user.last_name = ' '.join(partes[1:]) if len(partes) > 1 else ''
        
        request.user.email = request.POST.get('email', '')
        request.user.save()
        
        # Dados do perfil
        perfil.bio = request.POST.get('bio', '')
        perfil.localizacao = request.POST.get('location', '')
        perfil.filme_favorito = request.POST.get('favoriteMovie', '')
        perfil.perfil_publico = request.POST.get('publicProfile') == 'on'
        perfil.mostrar_estante = request.POST.get('showLibrary') == 'on'
        perfil.notificacoes = request.POST.get('notifications') == 'on'
        
        # Upload da foto
        if 'foto' in request.FILES:
            perfil.foto = request.FILES['foto']
        
        perfil.save()
        
        messages.success(request, 'Perfil atualizado com sucesso!')
        return redirect('usuarios:editar_perfil')
    
    context = {
        'perfil': perfil,
        'user': request.user
    }
    
    return render(request, 'usuarios/editar.html', context)