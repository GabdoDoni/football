from django.db.models import Count

from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить игрока", 'url_name': 'add_player'},
        {'title': "Обратная связь", 'url_name': 'contact'},
]

class DataMixin:
    paginate_by = 2

    def get_user_context(self, **kwargs):
        context = kwargs
        comms = Community.objects.annotate(Count('players'))

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)

        context['menu'] = user_menu

        context['comms'] = comms
        if 'comms_selected' not in context:
            context['comms_selected'] = 0
        return context
