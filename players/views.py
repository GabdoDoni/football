from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import *
from .models import *
from .utils import *

# Create your views here.


class Home(DataMixin, ListView):
    model = Players
    template_name = 'players/index.html'
    context_object_name = 'player'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Главная страница")
        return dict(list(context.items()) + list(c_def.items()))


# def index(request):
#     player = Players.objects.all()
#     # comms = Community.objects.all()
#     context = {
#         'player': player,
#         # 'comms': comms,
#         # 'menu': menu,
#         'title': 'Главная страница',
#         # 'comm_selected': 0,
#     }
#     return render(request, 'players/index.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def about(request):
    return render(request, 'players/about.html', {'title': 'О сайте'})


class AddPlayer(DataMixin,CreateView):
    form_class = AddPlayerForm
    template_name = 'players/addplayer.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Главная страница")
        return dict(list(context.items()) + list(c_def.items()))


# def add_player(request):
#     if request.method == 'POST':
#         form = AddPlayerForm(request.POST, request.FILES)
#         if form.is_valid():
#             # print(form.cleaned_data)
#             form.save()
#             return redirect('home')
#             # except:
#             #     form.add_error(None, 'Ошибка')
#     else:
#         form = AddPlayerForm()
#
#     return render(request, 'players/addplayer.html', {'form': form, 'title': 'Добавить игрока'})


def contact(request):
    return render(request, 'players/about.html', {'title': 'Обратная связь'})


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'players/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'players/login.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')

# def login(request):
#     return render(request, 'players/about.html', {'title': 'Войти'})


def community(request, commid):
    return HttpResponse(f'Создана сообщество {commid}')


class ShowPlayer(DetailView):
    model = Players
    template_name = 'players/skills.html'
    slug_url_kwargs = 'player_slug'
    context_object_name = 'player'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['player']
        return context


# def show_post(request, player_slug):
#     player = get_object_or_404(Players, slug=player_slug)
#
#     context = {
#         'player': player,
#         'username': player.username,
#         'comm_selected': player.comm_id,
#     }
#
#     return render(request, 'players/skills.html', context=context)


class PlayerCommunity(ListView):
    model = Players
    template_name = 'players/index.html'
    context_object_name = 'player'
    allow_empty = False

    def get_queryset(self):
        return Players.objects.filter(comm__slug=self.kwargs['comm_slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Сообщества - ' + str(context['player'][0].comm)
        context['comm_selected'] = context['player'][0].comm_id
        return context


# def show_community(request, comm_id):
#     player = Players.objects.filter(comm_id=comm_id)
#     # comms = Community.objects.all()
#
#     if len(player) == 0:
#         raise Http404()
#
#     context = {
#         'player': player,
#         # 'comms': comms,
#         # 'menu': menu,
#         'title': 'Отображение по сообществам',
#         'comm_selected': comm_id,
#     }
#     return render(request, 'players/index.html', context=context)
#     # return HttpResponse(f'Создана комьюнити {comm_id}')


