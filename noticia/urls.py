from django.urls import path
from . import views


urlpatterns = [
    path('noticia/', views.noticia, name='noticia'),
]
