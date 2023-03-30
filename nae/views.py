from django.shortcuts import render

# Create your views here.


def nae(request):

    noticias = [
        {
            'titulo': 'Abertura EditalBolsa BAE',
            'imagem': 'nae/img/image 2.png',
            'descricao': '''Bolsa de Auxílio Estudantil (BAE),
foi aberta no ano de 2023 para que novos alunos possam concorrer
a bolsa no valor de 400 reais.''',
            'tempo': 'Publicado há 2 dias',
            'data': '09/01/2023',
            'last': False
        },
        {
            'titulo': 'Segunda Chamada Auxílio Residencial',
            'imagem': 'nae/img/image 2.png',
            'descricao': '''Mais 20 alunos alunos da lista de espera do auxílio
residencia foram chamados nessa Quarta feira para receberem a bolsa de 400 
reais.''',
            'tempo': 'Publicado há 3 horas',
            'data': '11/01/2023',
            'last': False
        },
        {
            'titulo': 'NAE promove evento musical',
            'imagem': 'nae/img/image 2.png',
            'descricao': '''O NAE em conjunto com alunos de vários cursos da 
universidade, realizaram um evento musical no Restaurante Universitáio nesta
sexta feira.''',
            'tempo': 'Publicado há 5 dias',
            'data': '06/01/2023',
            'last': False
        }

    ]

    return render(request, 'nae/page/nae.html', context={
        'noticias': noticias
    })
