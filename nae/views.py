from django.shortcuts import render

# Create your views here.


def nae(request):
    return render(request, 'nae/page/nae.html')
