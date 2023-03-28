from django.shortcuts import render

# Create your views here.


def noticia(request):

    noticia = {
        'titulo': '''Calouros do período 2023.1 tem até o final de Abril para 
matrículas''',
        'autor': 'João da Silva',
        'data': '2023-03-22',
        'categoria': 'Matrículas',
        'imagem': 'global/img/image 4.png',
        'conteudo': [
            '''Com o início do ano letivo de 2023, 
as universidades e faculdades de todo o país estão se 
preparando para receber seus novos alunos. Com isso, os
calouros do período 2023.1 têm até o final de abril para]
efetuarem suas matrículas. É importante que os estudantes
fiquem atentos aos prazos estabelecidos pelas instituições 
de ensino, para que possam garantir sua vaga no curso
desejado.''',
            '''Para realizar a matrícula, os calouros devem estar com
a documentação em dia e seguir as instruções fornecidas pela instituição de
ensino. Algumas universidades e faculdades oferecem o serviço de matrícula
online, o que torna o processo mais fácil e ágil. É importante lembrar que,
em algumas instituições, a matrícula só é efetivada após o pagamento da
primeira parcela da mensalidade.'''
        ],
    }

    comentarios = [
        {
            'nome': 'João Pereira ',
            'data': '2023-03-22',
            'conteudo': 'Muito obrigado pela informação, vou ficar de olho.'
        },
    ]

    return render(request, 'noticia/page/noticia.html', context={
        'noticia': noticia,
        'comentarios': comentarios,
    })
