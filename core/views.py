from django.shortcuts import render


# Create your views here.
def home(request):
    noticias = [
        {
            "titulo": "Nutrição UFPI",
            "imagem": "home/img/image 2.png",
            "descricao": """Curso de Nutrição abre campanha para ajudar os
estudantes a se alimentaram melhor no seu dia a dia.""",
            "tempo": "Postado há 16 horas",
            "data": "10/01/2023",
            "last": False,
        },
        {
            "titulo": "Sistemas de Informação UFPI",
            "imagem": "home/img/image 1.png",
            "descricao": """Professores do curso de Sistemas de Informação,
abrem vagas com bolsas para projetos de iniciação Científica e Tecnológica.""",
            "tempo": "Postado há 2 dias",
            "data": "08/01/2023",
            "last": False,
        },
        {
            "titulo": "Medicina UFPI",
            "imagem": "home/img/image 3.png",
            "descricao": """Curso de medicina abre 20 vagas de estágio em
hospitais e postos de saúde para os alunos poderem vivenciar na prática seus
aprendizados.""",
            "tempo": "Postado há 6 dias",
            "data": "04/01/2023",
            "last": True,
        },
    ]

    return render(request, "home/page/home.html", context={"noticias": noticias})


def contato(request):
    return render(request, "contato/page/contato.html")


def login(request):
    return render(request, "login/pages/login.html")


def nae(request):
    noticias = [
        {
            "titulo": "Abertura EditalBolsa BAE",
            "imagem": "nae/img/image 2.png",
            "descricao": """Bolsa de Auxílio Estudantil (BAE),
foi aberta no ano de 2023 para que novos alunos possam concorrer
a bolsa no valor de 400 reais.""",
            "tempo": "Publicado há 2 dias",
            "data": "09/01/2023",
            "last": False,
        },
        {
            "titulo": "Segunda Chamada Auxílio Residencial",
            "imagem": "nae/img/image 2.png",
            "descricao": """Mais 20 alunos alunos da lista de espera do auxílio
residencia foram chamados nessa Quarta feira para receberem a bolsa de 400 
reais.""",
            "tempo": "Publicado há 3 horas",
            "data": "11/01/2023",
            "last": False,
        },
        {
            "titulo": "NAE promove evento musical",
            "imagem": "nae/img/image 2.png",
            "descricao": """O NAE em conjunto com alunos de vários cursos da 
universidade, realizaram um evento musical no Restaurante Universitáio nesta
sexta feira.""",
            "tempo": "Publicado há 5 dias",
            "data": "06/01/2023",
            "last": False,
        },
    ]

    return render(request, "nae/page/nae.html", context={"noticias": noticias})


def noticia(request):
    noticia = {
        "titulo": """Calouros do período 2023.1 tem até o final de Abril para 
matrículas""",
        "autor": "João da Silva",
        "data": "2023-03-22",
        "categoria": "Matrículas",
        "imagem": "global/img/image 4.png",
        "conteudo": [
            """Com o início do ano letivo de 2023, 
as universidades e faculdades de todo o país estão se 
preparando para receber seus novos alunos. Com isso, os
calouros do período 2023.1 têm até o final de abril para]
efetuarem suas matrículas. É importante que os estudantes
fiquem atentos aos prazos estabelecidos pelas instituições 
de ensino, para que possam garantir sua vaga no curso
desejado.""",
            """Para realizar a matrícula, os calouros devem estar com
a documentação em dia e seguir as instruções fornecidas pela instituição de
ensino. Algumas universidades e faculdades oferecem o serviço de matrícula
online, o que torna o processo mais fácil e ágil. É importante lembrar que,
em algumas instituições, a matrícula só é efetivada após o pagamento da
primeira parcela da mensalidade.""",
        ],
    }

    comentarios = [
        {
            "nome": "João Pereira ",
            "data": "2023-03-22",
            "conteudo": "Muito obrigado pela informação, vou ficar de olho.",
        },
    ]

    return render(
        request,
        "noticia/page/noticia.html",
        context={
            "noticia": noticia,
            "comentarios": comentarios,
        },
    )


def sobre(request):
    devs = [
        {
            "way": "sobre/img/Ellipse 3.png",
            "nome": "João Vitor Moreira Passos",
            "linkedin": "https://www.linkedin.com/in/jo%C3%A3o-vitor-moreira-passos-37ab40206/",
        },
        {
            "way": "sobre/img/Ellipse 4.png",
            "nome": "João Victor de Lima ",
            "linkedin": False,
        },
        {
            "way": "sobre/img/Ellipse 5.png",
            "nome": "Dayan Ramos Gomes",
            "linkedin": "https://www.linkedin.com/in/dayan-gomes-129087213/",
        },
    ]
    devs[-1]["last"] = True
    return render(
        request,
        "sobre/page/sobre.html",
        context={
            "devs": devs,
        },
    )


def galeria(request):
    urls = [
        "galeria/imgs/image 1.png",
        "galeria/imgs/image 2.png",
        "galeria/imgs/image 3.png",
        "galeria/imgs/WhatsApp Image 2023-03-28 at 23.29 1.png",
        "galeria/imgs/WhatsApp Image 2023-03-28 at 23.29 2.png",
        "galeria/imgs/WhatsApp Image 2023-03-28 at 23.29 3.png",
        "galeria/imgs/WhatsApp Image 2023-03-28 at 23.36 1.png",
        "galeria/imgs/WhatsApp Image 2023-03-28 at 23.37 1.png",
        "galeria/imgs/WhatsApp Image 2023-03-28 at 23.37 2.png",
    ]

    return render(
        request,
        "galeria/page/galeria.html",
        context={
            "images": urls,
        },
    )
