
from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('add_player/', add_player, name='add_player'),
    path('contact', contact, name='contact'),
    path('login', login, name='login'),
    path('player/<int:player_id>/', show_player, name='player'),
]