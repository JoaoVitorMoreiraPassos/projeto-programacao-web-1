from django.urls import path
from . import views

urlpatterns = [
    path('NAE/', views.nae, name='nae')
]
