
from django.urls import path

from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('about/', about, name='about'),
    path('add_player/', AddPlayer.as_view(), name='add_player'),
    path('contact/', contact, name='contact'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('player/<player_slug>/', ShowPlayer.as_view(), name='player'),
    path('community/<slug:comm_slug>/', PlayerCommunity.as_view(), name='community'),
]