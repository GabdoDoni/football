from django import template
from players.models import *

register = template.Library()


@register.simple_tag(name='getcomms')
def get_community(filter=None):
    if not filter:
        return Community.objects.all()
    else:
        return Community.objects.filter(slug=filter)


@register.inclusion_tag('players/list_community.html')
def show_community(sort=None, comm_selected=0):
    if not sort:
        comms = Community.objects.all()
    else:
        comms = Community.objects.order_by(sort)

    return {'comms': comms, 'comm_selected': comm_selected}
