from django.shortcuts import render

# Create your views here.


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

    return render(request, 'galeria/page/galeria.html', context={
        'images': urls,
    })
