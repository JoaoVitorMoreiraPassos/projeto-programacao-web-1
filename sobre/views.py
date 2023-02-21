from django.shortcuts import render

# Create your views here.


def sobre(request):
    devs = [
        {
            "way": "sobre/img/Ellipse 3.png",
            "nome": "João Vitor Moreira Passos"
        },
        {
            "way": "sobre/img/Ellipse 4.png",
            "nome": "João Victor de Lima "
        },
        {
            "way": "sobre/img/Ellipse 5.png",
            "nome": "Dayan Ramos Gomes"
        },
    ]
    devs[-1]["last"] = True
    return render(request, 'sobre/page/sobre.html', context={
        "devs": devs,
    })
