from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.home, name="home"),
    path("contato/", views.contato, name="contato"),
    path("login/", views.login, name="login"),
    path("nae/", views.nae, name="nae"),
    path("noticias/", views.noticia, name="noticia"),
    path("sobre/", views.sobre, name="sobre"),
    path("galeria/", views.galeria, name="galeria"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
