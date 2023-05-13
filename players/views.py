from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import *

# Create your views here.

menu = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Добавить игрока', 'url_name': 'add_player'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        {'title': 'Войти', 'url_name': 'login'}
]


def index(request):
    posts = Players.objects.all()
    # comms = Community.objects.all()
    context = {
        'posts': posts,
        # 'comms': comms,
        'menu': menu,
        'title': 'Главная страница',
        'comm_selected': 0,
    }
    return render(request, 'players/index.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def about(request):
    return render(request, 'players/about.html', {'menu': menu, 'title': 'О сайте'})


def add_player(request):
    return render(request, 'players/about.html', {'menu': menu, 'title': 'О сайте'})


def contact(request):
    return render(request, 'players/about.html', {'menu': menu, 'title': 'О сайте'})


def login(request):
    return render(request, 'players/about.html', {'menu': menu, 'title': 'О сайте'})


def community(request, commid):
    return HttpResponse(f'Создана сообщество {commid}')


def show_player(request, player_id):
    return HttpResponse(f'Создана игрок {player_id}')


def show_community(request, comm_id):
    posts = Players.objects.filter(comm_id=comm_id)
    # comms = Community.objects.all()

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        # 'comms': comms,
        'menu': menu,
        'title': 'Отображение по рубрикам',
        'comm_selected': comm_id,
    }
    return render(request, 'players/index.html', context=context)
    # return HttpResponse(f'Создана комьюнити {comm_id}')


