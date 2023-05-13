from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("contato/", views.contato, name="contato"),
    path("login/", views.login, name="login"),
    path("nae/", views.nae, name="nae"),
    path("noticias/", views.noticia, name="noticia"),
    path("sobre/", views.sobre, name="sobre"),
    path("galeria/", views.galeria, name="galeria"),
]
