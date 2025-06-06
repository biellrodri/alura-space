from django.shortcuts import render  # noqa: F401


def index(request):
    return render(request, 'galeria/index.html')


def imagem(request):
    return render(request, 'galeria/imagem.html')
