from django.shortcuts import render

# Create your views here.


def sobre(request):
    devs = [
        {
            "way": "sobre/img/Ellipse 3.png",
            "nome": "João Vitor Moreira Passos",
            "linkedin": "https://www.linkedin.com/in/jo%C3%A3o-vitor-moreira-passos-37ab40206/"
        },
        {
            "way": "sobre/img/Ellipse 4.png",
            "nome": "João Victor de Lima ",
            "linkedin": False
        },
        {
            "way": "sobre/img/Ellipse 5.png",
            "nome": "Dayan Ramos Gomes",
            "linkedin": "https://www.linkedin.com/in/dayan-gomes-129087213/"
        },
    ]
    devs[-1]["last"] = True
    return render(request, 'sobre/page/sobre.html', context={
        "devs": devs,
    })
