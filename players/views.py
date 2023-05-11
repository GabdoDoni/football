from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import *

# Create your views here.

menu = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Добавить игрока', 'url_name': 'add_player'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        {'title': 'Войти', 'url_name': 'login'}
]


def index(request):
    posts = Players.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Главная страница'
    }
    return render(request, 'players/index.html', context= context)


def about(request):
    return render(request, 'players/about.html', {'menu': menu, 'title': 'О сайте'})


def add_player(request):
    return render(request, 'players/about.html', {'menu': menu, 'title': 'О сайте'})


def contact(request):
    return render(request, 'players/about.html', {'menu': menu, 'title': 'О сайте'})


def login(request):
    return render(request, 'players/about.html', {'menu': menu, 'title': 'О сайте'})


def community(request, commid):
    return HttpResponse(f'Создана комьюнити {commid}')


def show_player(request, player_id):
    return HttpResponse(f'Создана комьюнити {player_id}')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')