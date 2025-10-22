# filmes/management/commands/popular_filmes.py
# Este script popula o banco com filmes de exemplo

from django.core.management.base import BaseCommand
from filmes.models import Filme

class Command(BaseCommand):
    help = 'Popula o banco de dados com filmes de exemplo'

    def handle(self, *args, **kwargs):
        filmes_data = [
            {
                'titulo': 'Interestelar',
                'titulo_original': 'Interstellar',
                'ano': 2014,
                'genero': 'ficcao_cientifica',
                'duracao': '2h 49min',
                'sinopse': 'Uma equipe de exploradores viaja através de um buraco de minhoca no espaço em uma tentativa de garantir a sobrevivência da humanidade.',
                'diretor': 'Christopher Nolan',
                'elenco': 'Matthew McConaughey, Anne Hathaway, Jessica Chastain',
                'poster_url': 'https://image.tmdb.org/t/p/w500/gEU2QniE6E77NI6lCU6MxlNBvIx.jpg',
                'nota_imdb': 8.6
            },
            {
                'titulo': 'O Poderoso Chefão',
                'titulo_original': 'The Godfather',
                'ano': 1972,
                'genero': 'drama',
                'duracao': '2h 55min',
                'sinopse': 'O patriarca idoso de uma dinastia do crime organizado transfere o controle de seu império clandestino para seu filho relutante.',
                'diretor': 'Francis Ford Coppola',
                'elenco': 'Marlon Brando, Al Pacino, James Caan',
                'poster_url': 'https://image.tmdb.org/t/p/w500/3bhkrj58Vtu7enYsRolD1fZdja1.jpg',
                'nota_imdb': 9.2
            },
            {
                'titulo': 'A Origem',
                'titulo_original': 'Inception',
                'ano': 2010,
                'genero': 'ficcao_cientifica',
                'duracao': '2h 28min',
                'sinopse': 'Um ladrão que rouba segredos corporativos através do uso da tecnologia de compartilhamento de sonhos recebe a tarefa inversa de plantar uma ideia.',
                'diretor': 'Christopher Nolan',
                'elenco': 'Leonardo DiCaprio, Joseph Gordon-Levitt, Elliot Page',
                'poster_url': 'https://image.tmdb.org/t/p/w500/9gk7adHYeDvHkCSEqAvQNLV5Uge.jpg',
                'nota_imdb': 8.8
            },
            {
                'titulo': 'Parasita',
                'titulo_original': 'Gisaengchung',
                'ano': 2019,
                'genero': 'suspense',
                'duracao': '2h 12min',
                'sinopse': 'Ganância e discriminação de classes ameaçam a relação simbiótica recém-formada entre a família rica Parks e o clã indigente Kims.',
                'diretor': 'Bong Joon Ho',
                'elenco': 'Song Kang-ho, Lee Sun-kyun, Cho Yeo-jeong',
                'poster_url': 'https://image.tmdb.org/t/p/w500/7IiTTgloJzvGI1TAYymCfbfl3vT.jpg',
                'nota_imdb': 8.6
            },
            {
                'titulo': 'Vingadores: Ultimato',
                'titulo_original': 'Avengers: Endgame',
                'ano': 2019,
                'genero': 'acao',
                'duracao': '3h 1min',
                'sinopse': 'Após os eventos devastadores de Guerra Infinita, os Vingadores se reúnem mais uma vez para reverter as ações de Thanos.',
                'diretor': 'Anthony Russo, Joe Russo',
                'elenco': 'Robert Downey Jr., Chris Evans, Mark Ruffalo',
                'poster_url': 'https://image.tmdb.org/t/p/w500/q6y0Go1tsGEsmtFryDOJo3dEmqu.jpg',
                'nota_imdb': 8.4
            },
            {
                'titulo': 'Matrix',
                'titulo_original': 'The Matrix',
                'ano': 1999,
                'genero': 'ficcao_cientifica',
                'duracao': '2h 16min',
                'sinopse': 'Um hacker descobre a verdadeira natureza de sua realidade e seu papel na guerra contra seus controladores.',
                'diretor': 'Lana Wachowski, Lilly Wachowski',
                'elenco': 'Keanu Reeves, Laurence Fishburne, Carrie-Anne Moss',
                'poster_url': 'https://image.tmdb.org/t/p/w500/f89U3ADr1oiB1s9GkdPOEpXUk5H.jpg',
                'nota_imdb': 8.7
            },
            {
                'titulo': 'Pulp Fiction: Tempo de Violência',
                'titulo_original': 'Pulp Fiction',
                'ano': 1994,
                'genero': 'drama',
                'duracao': '2h 34min',
                'sinopse': 'As vidas de dois assassinos da máfia, um boxeador, a esposa de um gângster e um par de bandidos se entrelaçam.',
                'diretor': 'Quentin Tarantino',
                'elenco': 'John Travolta, Uma Thurman, Samuel L. Jackson',
                'poster_url': 'https://image.tmdb.org/t/p/w500/d5iIlFn5s0ImszYzBPb8JPIfbXD.jpg',
                'nota_imdb': 8.9
            },
            {
                'titulo': 'Coringa',
                'titulo_original': 'Joker',
                'ano': 2019,
                'genero': 'drama',
                'duracao': '2h 2min',
                'sinopse': 'Em Gotham City, Arthur Fleck, um comediante fracassado, se transforma no criminoso conhecido como Coringa.',
                'diretor': 'Todd Phillips',
                'elenco': 'Joaquin Phoenix, Robert De Niro, Zazie Beetz',
                'poster_url': 'https://image.tmdb.org/t/p/w500/udDclJoHjfjb8Ekgsd4FDteOkCU.jpg',
                'nota_imdb': 8.4
            },
            {
                'titulo': 'Duna',
                'titulo_original': 'Dune',
                'ano': 2021,
                'genero': 'ficcao_cientifica',
                'duracao': '2h 35min',
                'sinopse': 'O filho de uma família nobre tenta vingar a morte de seu pai enquanto salva um planeta rico em especiarias.',
                'diretor': 'Denis Villeneuve',
                'elenco': 'Timothée Chalamet, Rebecca Ferguson, Zendaya',
                'poster_url': 'https://image.tmdb.org/t/p/w500/d5NXSklXo0qyIYkgV94XAgMIckC.jpg',
                'nota_imdb': 8.0
            },
            {
                'titulo': 'Clube da Luta',
                'titulo_original': 'Fight Club',
                'ano': 1999,
                'genero': 'drama',
                'duracao': '2h 19min',
                'sinopse': 'Um funcionário de escritório insone e um fabricante de sabão formam um clube de luta clandestino.',
                'diretor': 'David Fincher',
                'elenco': 'Brad Pitt, Edward Norton, Helena Bonham Carter',
                'poster_url': 'https://image.tmdb.org/t/p/w500/pB8BM7pdSp6B6Ih7QZ4DrQ3PmJK.jpg',
                'nota_imdb': 8.8
            },
            {
                'titulo': 'Forrest Gump',
                'titulo_original': 'Forrest Gump',
                'ano': 1994,
                'genero': 'drama',
                'duracao': '2h 22min',
                'sinopse': 'As presidências de Kennedy e Johnson, a Guerra do Vietnã e outros eventos históricos se desenrolam através da perspectiva de um homem do Alabama.',
                'diretor': 'Robert Zemeckis',
                'elenco': 'Tom Hanks, Robin Wright, Gary Sinise',
                'poster_url': 'https://image.tmdb.org/t/p/w500/saHP97rTPS5eLmrLQEcANmKrsFl.jpg',
                'nota_imdb': 8.8
            },
            {
                'titulo': 'O Senhor dos Anéis: O Retorno do Rei',
                'titulo_original': 'The Lord of the Rings: The Return of the King',
                'ano': 2003,
                'genero': 'aventura',
                'duracao': '3h 21min',
                'sinopse': 'Gandalf e Aragorn lideram o Mundo dos Homens contra o exército de Sauron para distrair seu olhar de Frodo e Sam.',
                'diretor': 'Peter Jackson',
                'elenco': 'Elijah Wood, Viggo Mortensen, Ian McKellen',
                'poster_url': 'https://image.tmdb.org/t/p/w500/rCzpDGLbOoPwLjy3OAm5NUPOTrC.jpg',
                'nota_imdb': 9.0
            },
            # Adicione esses filmes na lista filmes_data do seu arquivo popular_filmes.py
# Cole ANTES do último ] (colchete de fechamento)

{
    'titulo': 'Cidade de Deus',
    'titulo_original': 'City of God',
    'ano': 2002,
    'genero': 'drama',
    'duracao': '2h 10min',
    'sinopse': 'Na Cidade de Deus, favela carioca, dois jovens crescem em caminhos opostos: um vira fotógrafo, o outro um poderoso traficante.',
    'diretor': 'Fernando Meirelles',
    'elenco': 'Alexandre Rodrigues, Leandro Firmino, Matheus Nachtergaele',
    'poster_url': 'https://image.tmdb.org/t/p/w500/k7eYdwVEqx77RZvXnOXuGhELRj.jpg',
    'nota_imdb': 8.6
},
{
    'titulo': 'Toy Story',
    'titulo_original': 'Toy Story',
    'ano': 1995,
    'genero': 'aventura',
    'duracao': '1h 21min',
    'sinopse': 'Um cowboy de brinquedo fica com ciúmes quando um novo brinquedo espacial toma seu lugar como o favorito de um menino.',
    'diretor': 'John Lasseter',
    'elenco': 'Tom Hanks, Tim Allen, Don Rickles',
    'poster_url': 'https://image.tmdb.org/t/p/w500/uXDfjJbdP4ijW5hWSBrPrlKpxab.jpg',
    'nota_imdb': 8.3
},
{
    'titulo': 'O Iluminado',
    'titulo_original': 'The Shining',
    'ano': 1980,
    'genero': 'terror',
    'duracao': '2h 26min',
    'sinopse': 'Uma família se muda para um hotel isolado onde uma presença sinistra influencia o pai à violência.',
    'diretor': 'Stanley Kubrick',
    'elenco': 'Jack Nicholson, Shelley Duvall, Danny Lloyd',
    'poster_url': 'https://image.tmdb.org/t/p/w500/xazWoLealQwEgqZ89MLZklLZD3k.jpg',
    'nota_imdb': 8.4
},
{
    'titulo': 'Parasita',
    'titulo_original': 'Parasite',
    'ano': 2019,
    'genero': 'suspense',
    'duracao': '2h 12min',
    'sinopse': 'Uma família pobre se infiltra na casa de uma família rica, mas um segredo obscuro ameaça destruir suas vidas.',
    'diretor': 'Bong Joon-ho',
    'elenco': 'Song Kang-ho, Lee Sun-kyun, Cho Yeo-jeong',
    'poster_url': 'https://image.tmdb.org/t/p/w500/7IiTTgloJzvGI1TAYymCfbfl3vT.jpg',
    'nota_imdb': 8.5
},
{
    'titulo': 'De Volta para o Futuro',
    'titulo_original': 'Back to the Future',
    'ano': 1985,
    'genero': 'ficcao_cientifica',
    'duracao': '1h 56min',
    'sinopse': 'Um adolescente viaja acidentalmente para 1955 em uma máquina do tempo e precisa garantir que seus pais se apaixonem.',
    'diretor': 'Robert Zemeckis',
    'elenco': 'Michael J. Fox, Christopher Lloyd, Lea Thompson',
    'poster_url': 'https://image.tmdb.org/t/p/w500/fNOH9f1aA7XRTzl1sAOx9iF553Q.jpg',
    'nota_imdb': 8.5
},
{
    'titulo': 'Coringa',
    'titulo_original': 'Joker',
    'ano': 2019,
    'genero': 'drama',
    'duracao': '2h 2min',
    'sinopse': 'Um comediante fracassado mergulha na loucura e se torna um ícone criminoso em Gotham City.',
    'diretor': 'Todd Phillips',
    'elenco': 'Joaquin Phoenix, Robert De Niro, Zazie Beetz',
    'poster_url': 'https://image.tmdb.org/t/p/w500/udDclJoHjfjb8Ekgsd4FDteOkCU.jpg',
    'nota_imdb': 8.4
},
{
    'titulo': 'Interestelar',
    'titulo_original': 'Interstellar',
    'ano': 2014,
    'genero': 'ficcao_cientifica',
    'duracao': '2h 49min',
    'sinopse': 'Uma equipe de exploradores viaja através de um buraco de minhoca no espaço para garantir a sobrevivência da humanidade.',
    'diretor': 'Christopher Nolan',
    'elenco': 'Matthew McConaughey, Anne Hathaway, Jessica Chastain',
    'poster_url': 'https://image.tmdb.org/t/p/w500/gEU2QniE6E77NI6lCU6MxlNBvIx.jpg',
    'nota_imdb': 8.6
},
{
    'titulo': 'Pantera Negra',
    'titulo_original': 'Black Panther',
    'ano': 2018,
    'genero': 'acao',
    'duracao': '2h 14min',
    'sinopse': 'T\'Challa retorna a Wakanda para assumir o trono, mas enfrenta um desafiante que ameaça o futuro da nação.',
    'diretor': 'Ryan Coogler',
    'elenco': 'Chadwick Boseman, Michael B. Jordan, Lupita Nyong\'o',
    'poster_url': 'https://image.tmdb.org/t/p/w500/uxzzxijgPIY7slzFvMotPv8wjKA.jpg',
    'nota_imdb': 7.3
},
{
    'titulo': 'O Auto da Compadecida',
    'titulo_original': 'O Auto da Compadecida',
    'ano': 2000,
    'genero': 'comedia',
    'duracao': '1h 44min',
    'sinopse': 'João Grilo e Chicó enfrentam o cangaceiro Severino e chegam até o julgamento final após a morte.',
    'diretor': 'Guel Arraes',
    'elenco': 'Matheus Nachtergaele, Selton Mello, Rogério Cardoso',
    'poster_url': 'https://image.tmdb.org/t/p/w500/oMm36vN2sWB8XKxmLxqlaPY20YK.jpg',
    'nota_imdb': 8.6
},
{
    'titulo': 'Tropa de Elite',
    'titulo_original': 'Tropa de Elite',
    'ano': 2007,
    'genero': 'acao',
    'duracao': '1h 55min',
    'sinopse': 'Capitão Nascimento do BOPE busca um substituto enquanto enfrenta a corrupção e o tráfico de drogas no Rio de Janeiro.',
    'diretor': 'José Padilha',
    'elenco': 'Wagner Moura, Caio Junqueira, André Ramiro',
    'poster_url': 'https://image.tmdb.org/t/p/w500/6kM5tPWjqGPxvXQVlYOmKhCV4FH.jpg',
    'nota_imdb': 8.0
},
{
    'titulo': 'Se Beber, Não Case!',
    'titulo_original': 'The Hangover',
    'ano': 2009,
    'genero': 'comedia',
    'duracao': '1h 40min',
    'sinopse': 'Três amigos acordam após uma despedida de solteiro em Las Vegas sem memória e precisam encontrar o noivo desaparecido.',
    'diretor': 'Todd Phillips',
    'elenco': 'Bradley Cooper, Ed Helms, Zach Galifianakis',
    'poster_url': 'https://image.tmdb.org/t/p/w500/aJJNqZJqY5VEquQJfnB7AYPJHfH.jpg',
    'nota_imdb': 7.7
},
{
    'titulo': 'Invocação do Mal',
    'titulo_original': 'The Conjuring',
    'ano': 2013,
    'genero': 'terror',
    'duracao': '1h 52min',
    'sinopse': 'Investigadores paranormais Ed e Lorraine Warren ajudam uma família aterrorizada por uma entidade obscura em sua fazenda.',
    'diretor': 'James Wan',
    'elenco': 'Vera Farmiga, Patrick Wilson, Lili Taylor',
    'poster_url': 'https://image.tmdb.org/t/p/w500/wVYREutTvI2tmxr6ujrHT704wGF.jpg',
    'nota_imdb': 7.5
},
{
    'titulo': 'Gladiador',
    'titulo_original': 'Gladiator',
    'ano': 2000,
    'genero': 'acao',
    'duracao': '2h 35min',
    'sinopse': 'Um general romano traído se torna gladiador e busca vingança contra o corrupto imperador que assassinou sua família.',
    'diretor': 'Ridley Scott',
    'elenco': 'Russell Crowe, Joaquin Phoenix, Connie Nielsen',
    'poster_url': 'https://image.tmdb.org/t/p/w500/ty8TGRuvJLPUmAR1H1nRIsgwvim.jpg',
    'nota_imdb': 8.5
},
{
    'titulo': 'Wall-E',
    'titulo_original': 'WALL-E',
    'ano': 2008,
    'genero': 'aventura',
    'duracao': '1h 38min',
    'sinopse': 'Um robô solitário encarregado de limpar a Terra abandonada se apaixona e embarca em uma jornada espacial.',
    'diretor': 'Andrew Stanton',
    'elenco': 'Ben Burtt, Elissa Knight, Jeff Garlin',
    'poster_url': 'https://image.tmdb.org/t/p/w500/hbhFnRzzg6ZDmm8YAmxBnQpQIPh.jpg',
    'nota_imdb': 8.4
},
{
    'titulo': 'Clube da Luta',
    'titulo_original': 'Fight Club',
    'ano': 1999,
    'genero': 'drama',
    'duracao': '2h 19min',
    'sinopse': 'Um insone conhece um vendedor carismático e juntos formam um clube de luta clandestino que evolui para algo mais.',
    'diretor': 'David Fincher',
    'elenco': 'Brad Pitt, Edward Norton, Helena Bonham Carter',
    'poster_url': 'https://image.tmdb.org/t/p/w500/pB8BM7pdSp6B6Ih7QZ4DrQ3PmJK.jpg',
    'nota_imdb': 8.8
},
{
    'titulo': 'Divertida Mente',
    'titulo_original': 'Inside Out',
    'ano': 2015,
    'genero': 'aventura',
    'duracao': '1h 35min',
    'sinopse': 'As emoções personificadas de uma menina lutam para ajudá-la a se adaptar à nova vida após uma mudança.',
    'diretor': 'Pete Docter',
    'elenco': 'Amy Poehler, Phyllis Smith, Bill Hader',
    'poster_url': 'https://image.tmdb.org/t/p/w500/2H1TmgdfNtsKlU9jKdeNyYL5y8T.jpg',
    'nota_imdb': 8.1
},
{
    'titulo': 'Amor à Meia-Noite',
    'titulo_original': 'Midnight in Paris',
    'ano': 2011,
    'genero': 'romance',
    'duracao': '1h 34min',
    'sinopse': 'Um escritor em Paris magicamente viaja para os anos 1920 todas as noites à meia-noite.',
    'diretor': 'Woody Allen',
    'elenco': 'Owen Wilson, Rachel McAdams, Marion Cotillard',
    'poster_url': 'https://image.tmdb.org/t/p/w500/4wBG5kbfagTQclETblPRRGihk0I.jpg',
    'nota_imdb': 7.6
},
{
    'titulo': 'Psicose',
    'titulo_original': 'Psycho',
    'ano': 1960,
    'genero': 'suspense',
    'duracao': '1h 49min',
    'sinopse': 'Uma secretária rouba dinheiro e se hospeda em um motel isolado administrado por um jovem perturbado.',
    'diretor': 'Alfred Hitchcock',
    'elenco': 'Anthony Perkins, Janet Leigh, Vera Miles',
    'poster_url': 'https://image.tmdb.org/t/p/w500/yz4QVqPx3h1hD1DfqqQkCq3rmxW.jpg',
    'nota_imdb': 8.5
},
{
    'titulo': 'La La Land',
    'titulo_original': 'La La Land',
    'ano': 2016,
    'genero': 'romance',
    'duracao': '2h 8min',
    'sinopse': 'Uma atriz aspirante e um músico de jazz se apaixonam enquanto perseguem seus sonhos em Los Angeles.',
    'diretor': 'Damien Chazelle',
    'elenco': 'Ryan Gosling, Emma Stone, John Legend',
    'poster_url': 'https://image.tmdb.org/t/p/w500/uDO8zWDhfWwoFdKS4fzkUJt0Rf0.jpg',
    'nota_imdb': 8.0
},
{
    'titulo': 'Corra!',
    'titulo_original': 'Get Out',
    'ano': 2017,
    'genero': 'terror',
    'duracao': '1h 44min',
    'sinopse': 'Um jovem negro descobre segredos perturbadores quando visita a família de sua namorada branca.',
    'diretor': 'Jordan Peele',
    'elenco': 'Daniel Kaluuya, Allison Williams, Bradley Whitford',
    'poster_url': 'https://image.tmdb.org/t/p/w500/tFXcEccSQMf3lfhfXKSU9iRBpa3.jpg',
    'nota_imdb': 7.7
},
        ]

        contador = 0
        for filme_data in filmes_data:
            filme, created = Filme.objects.get_or_create(
                titulo=filme_data['titulo'],
                ano=filme_data['ano'],
                defaults=filme_data
            )
            if created:
                contador += 1
                self.stdout.write(
                    self.style.SUCCESS(f'✓ Filme adicionado: {filme.titulo}')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'- Filme já existe: {filme.titulo}')
                )

        self.stdout.write(
            self.style.SUCCESS(f'\n🎬 Total de filmes adicionados: {contador}')
        )