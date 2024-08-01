from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

def index(request):
    return HttpResponse("<h2>Мой первый сайт</h2>")

def categories(request, catid):

    if request.GET:
        print(request.GET)
    return HttpResponse(f"<h2>Проверка категории</h2><p>{catid}</p>")

def pageNotFound(request, exception):
    return HttpResponseNotFound(f"<h2>Страница не найдена</h2> <p>{exception}</p>")