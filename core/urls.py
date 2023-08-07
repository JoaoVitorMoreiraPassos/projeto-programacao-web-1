from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = "core"

urlpatterns = [
    path("", views.home, name="home"),
    path("contato/", views.contato, name="contato"),
    path("login/", views.login_page, name="login_page"),
    path("login/authentication/", views.login_view, name="login_view"),
    path("nae/", views.nae, name="nae"),
    path("noticias/<slug:slug>/", views.noticia, name="noticia"),
    path("sobre/", views.sobre, name="sobre"),
    path("galeria/", views.galeria, name="galeria"),
    path("login/create_profile/", views.create_view, name="create_profile"),
    # path para a view comment
    path("noticias/comment/<slug:slug>/", views.comment, name="comment"),
    path("admin-ru/", views.admin_ru, name="admin_ru"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
