from django.shortcuts import render

# Create your views here.


def index(request):

    noticias = [
        {
            'titulo': 'Nutrição UFPI',
            'imagem': 'home/img/image 2.png',
            'descricao': '''Curso de Nutrição abre campanha para ajudar os
estudantes a se alimentaram melhor no seu dia a dia.''',
            'tempo': 'Postado há 16 horas',
            'data': '10/01/2023',
            'last': False
        },
        {
            'titulo': 'Sistemas de Informação UFPI',
            'imagem': 'home/img/image 1.png',
            'descricao': '''Professores do curso de Sistemas de Informação,
abrem vagas com bolsas para projetos de iniciação Científica e Tecnológica.''',
            'tempo': 'Postado há 2 dias',
            'data': '08/01/2023',
            'last': False
        },
        {
            'titulo': 'Medicina UFPI',
            'imagem': 'home/img/image 3.png',
            'descricao': '''Curso de medicina abre 20 vagas de estágio em
hospitais e postos de saúde para os alunos poderem vivenciar na prática seus
aprendizados.''',
            'tempo': 'Postado há 6 dias',
            'data': '04/01/2023',
            'last': True
        }
    ]

    return render(request, 'home/page/home.html', context={
        'noticias': noticias
    })
