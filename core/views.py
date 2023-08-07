from django.shortcuts import render
from .models import (
    Profile,
    Category,
    Notice,
    Comment,
    Ingredient,
    User,
    Recipe,
    RecipeDates,
)
from datetime import datetime
from django.http import Http404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.urls import reverse
from datetime import time, date, datetime
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def home(request):
    # get all news and order by date
    noticias = Notice.objects.all().order_by("-date_time")
    # get all categories
    meal = "ALMOÇO" if time(13, 30, 0) > datetime.now().time() else "JANTAR"
    # get all recipes
    cardapio = RecipeDates.objects.filter(date=date.today(), meal=meal).first()
    if cardapio:
        ingredients = Ingredient.objects.filter(recipe=cardapio.recipe.pk)
        cardapio.ingredients = ingredients
    for noticia in noticias:
        # converter data para formato %d de %B de %Y e traduzir para português
        noticia.date = datetime.strptime(
            str(noticia.date_time).split(".")[0], "%Y-%m-%d %H:%M:%S"
        ).strftime("%d de %B de %Y")
        noticia.date = noticia.date.replace("January", "Janeiro")
        noticia.date = noticia.date.replace("February", "Fevereiro")
        noticia.date = noticia.date.replace("March", "Março")
        noticia.date = noticia.date.replace("April", "Abril")
        noticia.date = noticia.date.replace("May", "Maio")
        noticia.date = noticia.date.replace("June", "Junho")
        noticia.date = noticia.date.replace("July", "Julho")
        noticia.date = noticia.date.replace("August", "Agosto")
        noticia.date = noticia.date.replace("September", "Setembro")
        noticia.date = noticia.date.replace("October", "Outubro")
        noticia.date = noticia.date.replace("November", "Novembro")
        noticia.date = noticia.date.replace("December", "Dezembro")
        # converter data para o um objeto datetime no formato brasileiro
        noticia.time_pass = datetime.now() - datetime.strptime(
            str(noticia.date_time).split(".")[0], "%Y-%m-%d %H:%M:%S"
        )
        if noticia.time_pass.days > 0:
            noticia.time_pass = f"Publicado há {noticia.time_pass.days} \
            dias"
        elif noticia.time_pass.seconds // 3600 > 0:
            noticia.time_pass = (
                f"Publicado há {noticia.time_pass.seconds // 3600} horas"
            )
        elif noticia.time_pass.seconds // 60 > 0:
            noticia.time_pass = (
                f"Publicado há {noticia.time_pass.seconds // 60} minutos"
            )
        else:
            noticia.time_pass = f"Publicado há {noticia.time_pass.seconds} \
            segundos"
        if noticia == noticias.last():
            noticia.last = True
    return render(
        request,
        "home/page/home.html",
        context={"noticias": noticias, "cardapio": cardapio},
    )


def contato(request):
    return render(request, "contato/page/contato.html")


def admin_ru(request):
    recipes = Recipe.objects.all()
    for recipe in recipes:
        print(recipe.title)
    context = {"recipes": recipes}
    return render(request, "admin/pages/ru.html", context)


def login_page(request):
    return render(request, "login/pages/login.html")


@csrf_exempt
def login_view(request):
    if not request.method == "POST":
        raise Http404("Invalid method")
    data = request.POST
    user = authenticate(username=data["email"], password=data["password"])
    if user is not None:
        login(request, user)

        return redirect(reverse("core:home"))
    else:
        return render(
            request,
            "login/pages/login.html",
            context={"message": "Invalid credentials"},
        )


# create profile is a class based view
def create_view(request):
    # this view will receive a POST request with the following data:
    # {"name": "name", "email": "email", "password": "password"}
    # and will create a profile and a user if the user doesn't exist

    if not request.method == "POST":
        raise Http404("Invalid method")
    data = request.POST
    # check if user already exists
    try:
        # if user exists, return a message
        user = User.objects.get(email=data["email"])
        return render(
            request,
            "login/pages/login.html",
            context={"message": "User already exists"},
        )
    except User.DoesNotExist:
        # if user doesn't exist, create a new user and profile
        user = User.objects.create_user(
            username=data["email"],
            first_name=data["name"].split(" ")[0],
            last_name=data["name"].split(" ")[1::],
            email=data["email"],
            password=data["password"],
        )
        profile = Profile.objects.create(user=user)
        profile.save()
        return render(
            request,
            "login/pages/login.html",
            context={"message": "User created"},
        )


def nae(request):
    # get all news and order by date
    noticias = Notice.objects.filter(category=Category.objects.get(name="NAE"))
    # get all categories
    for noticia in noticias:
        # converter data para formato %d de %B de %Y e traduzir para português
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
            noticia.time_pass = f"Publicado há {noticia.time_pass.seconds} \
                segundos"
        if noticia == noticias.last():
            noticia.last = True

    return render(request, "nae/page/nae.html", context={"noticias": noticias})


def noticia(request, slug):
    noticia = Notice.objects.get(slug=slug)
    # converter data para o um objeto datetime no formato brasileiro
    noticia.date = datetime.strptime(
        str(noticia.date_time).split(".")[0], "%Y-%m-%d %H:%M:%S"
    ).strftime("%d/%m/%Y")
    comentarios = Comment.objects.filter(notice=noticia)
    for comentario in comentarios:
        comentario.time_pass = datetime.now() - datetime.strptime(
            str(comentario.date).split(".")[0], "%Y-%m-%d %H:%M:%S"
        )
        if comentario.time_pass.days > 0:
            comentario.time_pass = f"Publicado há {comentario.time_pass.days} \
                dias"
        elif comentario.time_pass.seconds // 3600 > 0:
            comentario.time_pass = (
                f"Publicado há {comentario.time_pass.seconds // 3600} horas"
            )
        elif comentario.time_pass.seconds // 60 > 0:
            comentario.time_pass = (
                f"Publicado há {comentario.time_pass.seconds // 60} minutos"
            )
        else:
            comentario.time_pass = (
                f"Publicado há {comentario.time_pass.seconds} segundos"
            )
        if comentario == comentarios.last():
            comentario.last = True
    return render(
        request,
        "noticia/page/noticia.html",
        context={
            "noticia": noticia,
            "comentarios": comentarios,
        },
    )


@login_required(login_url="core:login_page", redirect_field_name="next")
def comment(request, slug):
    if not request.method == "POST":
        raise Http404("Invalid method")
    data = request.POST
    user = request.user
    noticia = Notice.objects.get(slug=slug)
    comment = Comment.objects.create(
        user=user,
        notice=noticia,
        content=data["comment"],
        date=datetime.now(),
    )
    comment.save()
    return redirect(reverse("core:noticia", kwargs={"slug": slug}))


def sobre(request):
    devs = [
        {
            "image": "sobre/img/Ellipse 3.png",
            "name": "João Vitor Moreira Passos",
            "linkedin": "https://www.linkedin.com/in/\
                jo%C3%A3o-vitor-moreira-passos-37ab40206/",
        },
        {
            "image": "sobre/img/Ellipse 5.png",
            "name": "Dayan Ramos Gomes",
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
