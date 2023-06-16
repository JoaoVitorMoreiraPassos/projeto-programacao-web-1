from django.shortcuts import render
from .models import Profile, Category, Notice, Comment, Recipe, Ingredient
from datetime import datetime


# Create your views here.
def home(request):
    noticias = Notice.objects.all().order_by("-date_time")
    cardapio = Recipe.objects.all()[0]
    cardapio.recipe = Ingredient.objects.filter(recipe=cardapio)
    cardapio.meal = "Almoço"
    for noticia in noticias:
        noticia.time_pass = datetime.now() - datetime.strptime(
            str(noticia.date_time).split(".")[0], "%Y-%m-%d %H:%M:%S"
        )
        if noticia.time_pass.days > 0:
            noticia.time_pass = f"Publicado há {noticia.time_pass.days} dias"
        elif noticia.time_pass.seconds // 3600 > 0:
            noticia.time_pass = (
                f"Publicado há {noticia.time_pass.seconds // 3600} horas"
            )
        elif noticia.time_pass.seconds // 60 > 0:
            noticia.time_pass = (
                f"Publicado há {noticia.time_pass.seconds // 60} minutos"
            )
        else:
            noticia.time_pass = f"Publicado há {noticia.time_pass.seconds} segundos"
        if noticia == noticias.last():
            noticia.last = True
    return render(
        request,
        "home/page/home.html",
        context={"noticias": noticias, "cardapio": cardapio},
    )


def contato(request):
    return render(request, "contato/page/contato.html")


def login(request):
    return render(request, "login/pages/login.html")


def nae(request):
    noticias = Notice.objects.filter(category=Category.objects.get(name="NAE"))

    for noticia in noticias:
        noticia.time_pass = datetime.now() - datetime.strptime(
            str(noticia.date_time).split(".")[0], "%Y-%m-%d %H:%M:%S"
        )
        if noticia.time_pass.days > 0:
            noticia.time_pass = f"Publicado há {noticia.time_pass.days} dias"
        elif noticia.time_pass.seconds // 3600 > 0:
            noticia.time_pass = (
                f"Publicado há {noticia.time_pass.seconds // 3600} horas"
            )
        elif noticia.time_pass.seconds // 60 > 0:
            noticia.time_pass = (
                f"Publicado há {noticia.time_pass.seconds // 60} minutos"
            )
        else:
            noticia.time_pass = f"Publicado há {noticia.time_pass.seconds} segundos"
        if noticia == noticias.last():
            noticia.last = True

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
