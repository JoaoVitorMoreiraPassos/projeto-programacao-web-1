from django.shortcuts import render

# Create your views here.


def contato(request):
    return render(request, 'contato/page/contato.html')
