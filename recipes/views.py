from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'recipes/home.html')
    # return HTTP Response


def contato(request):
    return render(request, 'recipes/contato.html')
    # return HTTP Response


def sobre(request):
    return HttpResponse('sobre')
    # return HTTP Response
