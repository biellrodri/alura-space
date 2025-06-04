from django.shortcuts import render  # noqa: F401
from django.http import HttpResponse


def index(request):
    return HttpResponse('<h1>Alura Space</h1><p>Seja bem-vindo ao espaço<p>')
