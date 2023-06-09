from django.contrib import admin
from .models import *

# Register your models here.

class PlayersAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'name', 'time_create')
    list_display_links = ('id', 'username')
    search_fields = ('username', 'comment')
    prepopulated_fields = {'slug': ('username',)}

class CommunityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name', )
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Players, PlayersAdmin)
admin.site.register(Community, CommunityAdmin)
