# filmes/views.py
import json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from .models import Filme, Estante, Comentario, Reacao

# =====================================================
# VIEWS ANTIGAS (Mantidas)
# =====================================================

@login_required
def editar_perfil(request):
    return render(request, 'perfil/editar.html')

@login_required
def lista_filmes(request):
    """Lista de filmes da estante do usuário"""
    filmes_estante = Estante.objects.filter(usuario=request.user).select_related('filme')
    
    context = {
        'filmes_estante': filmes_estante,
    }
    return render(request, 'filmes/lista.html', context)

@login_required
def buscar_filmes(request):
    return render(request, 'filmes/buscar.html')


# =====================================================
# HOME VIEW - MANTENDO OS FILMES ORIGINAIS DO CARROSSEL
# =====================================================

def home_view(request):
    """View da página inicial com filmes REALMENTE em cartaz em outubro 2025"""
    
    # Filmes EM CARTAZ REALMENTE (Outubro 2025) - MANTIDOS OS ORIGINAIS!
    # NOTA: Estes são dados estáticos para o carrossel, não vêm do banco
    filmes_cartaz = [
        {
            'id': 1,  # ID fictício para o link funcionar (vamos usar um filme real do banco)
            'titulo': 'Tron: Ares',
            'sinopse': 'Ares, um sofisticado programa de IA, é enviado do mundo digital para o mundo real em uma missão perigosa, marcando o primeiro encontro da humanidade com seres de Inteligência Artificial.',
            'genero': 'Ficção Científica',
            'ano': 2025,
            'duracao': '119 min',
            'nota': 6.7,
            'poster': 'https://www.themoviedb.org/t/p/w600_and_h900_bestv2/3Aijwt71AG3dtI5WoYG8g9dWfQI.jpg',
            'backdrop': 'https://image.tmdb.org/t/p/original/jUplF2dluebAYdHa901mhPVOZYU.jpg',
            'trailer_url': 'https://www.youtube.com/embed/_68tQpaTaIs',
        },
        {
            'id': 2,
            'titulo': 'Coração de Lutador',
            'sinopse': 'A história real de Mark Kerr, bicampeão dos pesos pesados do UFC, que enfrentou batalhas pessoais intensas fora do octógono, incluindo o vício em opioides.',
            'genero': 'Drama',
            'ano': 2025,
            'duracao': '123 min',
            'nota': 6.8,
            'poster': 'https://www.themoviedb.org/t/p/w600_and_h900_bestv2/270Y5jWtJMU8cK2Q8MSwJqsnUgS.jpg',
            'backdrop': 'https://image.tmdb.org/t/p/original/vfbryKoLrisx8Xh37OaTjTyrFY0.jpg',
            'trailer_url': 'https://www.youtube.com/embed/HJuS4baeaxU',
        },
        {
            'id': 3,
            'titulo': 'Paddington no Peru',
            'sinopse': 'Paddington e a família Brown embarcam em uma emocionante aventura na floresta amazônica do Peru em busca da lendária Cidade Perdida de Ouro.',
            'genero': 'Aventura',
            'ano': 2024,
            'duracao': '106 min',
            'nota': 7.3,
            'poster': 'https://image.tmdb.org/t/p/w500/arMd4W3rqkzYfwdCgZp72BF3Tof.jpg',
            'backdrop': 'https://image.tmdb.org/t/p/original/xi1VSt3DtkevUmzCx2mNlCoDe74.jpg',
            'trailer_url': 'https://www.youtube.com/embed/1o4rjI-z1vs',
        },
        {
            'id': 4,
            'titulo': 'Nosferatu',
            'sinopse': 'Uma jovem assombrada é atraída por um vampiro misterioso obcecado por ela, causando horror indescritível em seu caminho.',
            'genero': 'Terror',
            'ano': 2024,
            'duracao': '132 min',
            'nota': 7.3,
            'poster': 'https://image.tmdb.org/t/p/w500/qD45xHA35HdJDGOaA1AgDwiWEgO.jpg',
            'backdrop': 'https://image.tmdb.org/t/p/original/18TSJF1WLA4CkymvVUcKDBwUJ9F.jpg',
            'trailer_url': 'https://www.youtube.com/embed/moIrYMjS0nI',
        },
    ]
    
    # Top 10 Semanal - COM IDs CORRETOS DO BANCO
    top10_semanal = [
        {'id': 1, 'titulo': 'Interestelar', 'ano': 2014, 'nota': 8.7, 'poster': 'https://image.tmdb.org/t/p/w500/gEU2QniE6E77NI6lCU6MxlNBvIx.jpg', 'posicao': 1},
        {'id': 3, 'titulo': 'A Origem', 'ano': 2010, 'nota': 8.8, 'poster': 'https://image.tmdb.org/t/p/w500/9gk7adHYeDvHkCSEqAvQNLV5Uge.jpg', 'posicao': 2},
        {'id': 2, 'titulo': 'O Poderoso Chefão', 'ano': 1972, 'nota': 9.2, 'poster': 'https://image.tmdb.org/t/p/w500/3bhkrj58Vtu7enYsRolD1fZdja1.jpg', 'posicao': 3},
        {'id': 7, 'titulo': 'Pulp Fiction', 'ano': 1994, 'nota': 8.9, 'poster': 'https://image.tmdb.org/t/p/w500/d5iIlFn5s0ImszYzBPb8JPIfbXD.jpg', 'posicao': 4},
        {'id': 6, 'titulo': 'Matrix', 'ano': 1999, 'nota': 8.7, 'poster': 'https://image.tmdb.org/t/p/w500/f89U3ADr1oiB1s9GkdPOEpXUk5H.jpg', 'posicao': 5},
        {'id': 10, 'titulo': 'Clube da Luta', 'ano': 1999, 'nota': 8.8, 'poster': 'https://image.tmdb.org/t/p/w500/pB8BM7pdSp6B6Ih7QZ4DrQ3PmJK.jpg', 'posicao': 6},
        {'id': 11, 'titulo': 'Forrest Gump', 'ano': 1994, 'nota': 8.8, 'poster': 'https://image.tmdb.org/t/p/w500/arw2vcBveWOVZr6pxd9XTd1TdQa.jpg', 'posicao': 7},
        {'id': 12, 'titulo': 'O Senhor dos Anéis', 'ano': 2003, 'nota': 8.9, 'poster': 'https://image.tmdb.org/t/p/w500/6oom5QYQ2yQTMJIbnvbkBL9cHo6.jpg', 'posicao': 8},
        {'id': 8, 'titulo': 'Coringa', 'ano': 2019, 'nota': 8.4, 'poster': 'https://image.tmdb.org/t/p/w500/udDclJoHjfjb8Ekgsd4FDteOkCU.jpg', 'posicao': 9},
        {'id': 9, 'titulo': 'Duna', 'ano': 2021, 'nota': 8.0, 'poster': 'https://image.tmdb.org/t/p/w500/d5NXSklXo0qyIYkgV94XAgMIckC.jpg', 'posicao': 10},
    ]
    
    # Indicações - COM IDs CORRETOS DO BANCO
    indicacoes = [
        {'id': 13, 'titulo': 'Cidade de Deus', 'ano': 2002, 'genero': 'Drama', 'nota': 8.6, 'poster': 'https://upload.wikimedia.org/wikipedia/pt/1/10/CidadedeDeus.jpg'},
        {'id': 14, 'titulo': 'Toy Story', 'ano': 1995, 'genero': 'Animação', 'nota': 8.3, 'poster': 'https://image.tmdb.org/t/p/w500/uXDfjJbdP4ijW5hWSBrPrlKpxab.jpg'},
        {'id': 22, 'titulo': 'Gladiador', 'ano': 2000, 'genero': 'Ação', 'nota': 8.5, 'poster': 'https://image.tmdb.org/t/p/w500/ty8TGRuvJLPUmAR1H1nRIsgwvim.jpg'},
        {'id': 16, 'titulo': 'De Volta para o Futuro', 'ano': 1985, 'genero': 'Aventura', 'nota': 8.5, 'poster': 'https://image.tmdb.org/t/p/w500/fNOH9f1aA7XRTzl1sAOx9iF553Q.jpg'},
        {'id': 15, 'titulo': 'O Iluminado', 'ano': 1980, 'genero': 'Terror', 'nota': 8.4, 'poster': 'https://image.tmdb.org/t/p/w500/xazWoLealQwEgqZ89MLZklLZD3k.jpg'},
        {'id': 27, 'titulo': 'La La Land', 'ano': 2016, 'genero': 'Romance', 'nota': 8.0, 'poster': 'https://image.tmdb.org/t/p/w500/uDO8zWDhfWwoFdKS4fzkUJt0Rf0.jpg'},
    ]
    
    # Em Alta - COM IDs CORRETOS DO BANCO
    em_alta = [
        {'id': 5, 'titulo': 'Vingadores: Ultimato', 'ano': 2019, 'genero': 'Ação', 'nota': 8.4, 'poster': 'https://image.tmdb.org/t/p/w500/q6y0Go1tsGEsmtFryDOJo3dEmqu.jpg'},
        {'id': 20, 'titulo': 'Se Beber, Não Case!', 'ano': 2009, 'genero': 'Comédia', 'nota': 7.7, 'poster': 'https://m.media-amazon.com/images/I/618FiO7H+sS._AC_SY741_.jpg'},
        {'id': 4, 'titulo': 'Parasita', 'ano': 2019, 'genero': 'Drama', 'nota': 8.5, 'poster': 'https://image.tmdb.org/t/p/w500/7IiTTgloJzvGI1TAYymCfbfl3vT.jpg'},
        {'id': 17, 'titulo': 'Pantera Negra', 'ano': 2018, 'genero': 'Ação', 'nota': 7.3, 'poster': 'https://image.tmdb.org/t/p/w500/uxzzxijgPIY7slzFvMotPv8wjKA.jpg'},
        {'id': 23, 'titulo': 'Wall-E', 'ano': 2008, 'genero': 'Animação', 'nota': 8.1, 'poster': 'https://image.tmdb.org/t/p/w500/hbhFnRzzg6ZDmm8YAmxBnQpQIPh.jpg'},
        {'id': 24, 'titulo': 'Divertida Mente', 'ano': 2015, 'genero': 'Animação', 'nota': 8.1, 'poster': 'https://image.tmdb.org/t/p/w500/lRHE0vzf3oYJrhbsHXjIkF4Tl5A.jpg'},
    ]
    
    # Se usuário estiver logado, verifica quais filmes já estão na estante
    filmes_na_estante = []
    if request.user.is_authenticated:
        filmes_na_estante = list(Estante.objects.filter(usuario=request.user).values_list('filme_id', flat=True))
    
    context = {
        'filmes_cartaz': json.dumps(filmes_cartaz),
        'top10_semanal': top10_semanal,
        'indicacoes': indicacoes,
        'em_alta': em_alta,
        'filmes_na_estante': filmes_na_estante,
    }
    
    return render(request, 'home.html', context)


# =====================================================
# NOVAS VIEWS - Sistema de Filmes e Comentários
# =====================================================

@login_required
def filme_detalhes(request, filme_id):
    """Página de detalhes do filme com comentários"""
    
    # Busca o filme no banco
    filme = get_object_or_404(Filme, id=filme_id)
    
    # Verifica se usuário já tem na estante
    na_estante = Estante.objects.filter(usuario=request.user, filme=filme).exists()
    
    # Busca comentários do filme
    comentarios = filme.comentarios.select_related('usuario').all()
    
    # Para cada comentário, verifica se usuário curtiu
    for comentario in comentarios:
        comentario.usuario_curtiu_comentario = comentario.usuario_curtiu(request.user)
    
    context = {
        'filme': filme,
        'na_estante': na_estante,
        'comentarios': comentarios,
        'total_comentarios': comentarios.count(),
    }
    
    return render(request, 'filmes/detalhes.html', context)


@login_required
@require_POST
def adicionar_filme_estante(request, filme_id):
    """Adiciona filme à estante do usuário"""
    
    filme = get_object_or_404(Filme, id=filme_id)
    
    # Cria ou busca o item na estante
    estante, criado = Estante.objects.get_or_create(
        usuario=request.user,
        filme=filme,
        defaults={'status': 'quero_assistir'}
    )
    
    if criado:
        messages.success(request, f'"{filme.titulo}" foi adicionado à sua estante!')
    else:
        messages.info(request, f'"{filme.titulo}" já está na sua estante!')
    
    # Retorna JSON se for requisição AJAX
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({
            'success': True,
            'criado': criado,
            'message': f'"{filme.titulo}" foi adicionado à sua estante!' if criado else f'"{filme.titulo}" já está na sua estante!'
        })
    
    # Se não for AJAX, redireciona de volta
    return redirect(request.META.get('HTTP_REFERER', 'home'))


@login_required
@require_POST
def remover_filme_estante(request, filme_id):
    """Remove filme da estante do usuário"""
    
    filme = get_object_or_404(Filme, id=filme_id)
    
    try:
        estante = Estante.objects.get(usuario=request.user, filme=filme)
        estante.delete()
        messages.success(request, f'"{filme.titulo}" foi removido da sua estante!')
        sucesso = True
    except Estante.DoesNotExist:
        messages.warning(request, f'"{filme.titulo}" não está na sua estante!')
        sucesso = False
    
    # Retorna JSON se for requisição AJAX
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({'success': sucesso})
    
    return redirect(request.META.get('HTTP_REFERER', 'home'))


@login_required
@require_POST
def adicionar_comentario(request, filme_id):
    """Adiciona comentário ao filme"""
    
    filme = get_object_or_404(Filme, id=filme_id)
    texto = request.POST.get('texto', '').strip()
    
    if not texto:
        messages.error(request, 'O comentário não pode estar vazio!')
        return redirect('filmes:filme_detalhes', filme_id=filme_id)
    
    # Cria o comentário
    comentario = Comentario.objects.create(
        filme=filme,
        usuario=request.user,
        texto=texto
    )
    
    messages.success(request, 'Comentário adicionado com sucesso!')
    
    # Retorna JSON se for requisição AJAX
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({
            'success': True,
            'comentario': {
                'id': comentario.id,
                'texto': comentario.texto,
                'usuario': comentario.usuario.username,
                'foto_perfil': comentario.usuario.perfil.get_foto_url() if hasattr(comentario.usuario, 'perfil') else '',
                'data': comentario.data_criacao.strftime('%d/%m/%Y %H:%M'),
            }
        })
    
    return redirect('filmes:filme_detalhes', filme_id=filme_id)


@login_required
@require_POST
def curtir_comentario(request, comentario_id):
    """Curtir ou descurtir um comentário"""
    
    comentario = get_object_or_404(Comentario, id=comentario_id)
    
    # Verifica se já curtiu
    reacao = Reacao.objects.filter(comentario=comentario, usuario=request.user).first()
    
    if reacao:
        # Se já curtiu, remove a curtida
        reacao.delete()
        curtiu = False
        mensagem = 'Curtida removida!'
    else:
        # Se não curtiu, adiciona curtida
        Reacao.objects.create(
            comentario=comentario,
            usuario=request.user,
            tipo='curtida'
        )
        curtiu = True
        mensagem = 'Comentário curtido!'
    
    total_curtidas = comentario.total_curtidas()
    
    # Retorna JSON para AJAX
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({
            'success': True,
            'curtiu': curtiu,
            'total_curtidas': total_curtidas,
            'message': mensagem
        })
    
    messages.success(request, mensagem)
    return redirect('filmes:filme_detalhes', filme_id=comentario.filme.id)


@login_required
@require_POST
def deletar_comentario(request, comentario_id):
    """Deleta comentário (apenas o próprio usuário pode deletar)"""
    
    comentario = get_object_or_404(Comentario, id=comentario_id)
    
    # Verifica se o usuário é o dono do comentário
    if comentario.usuario != request.user:
        messages.error(request, 'Você não pode deletar este comentário!')
        return redirect('filmes:filme_detalhes', filme_id=comentario.filme.id)
    
    filme_id = comentario.filme.id
    comentario.delete()
    
    messages.success(request, 'Comentário deletado com sucesso!')
    
    # Retorna JSON se for requisição AJAX
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({'success': True})
    
    return redirect('filmes:filme_detalhes', filme_id=filme_id)