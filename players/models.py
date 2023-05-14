from django.db import models
from django.urls import reverse

# Create your models here.


class Players(models.Model):
    username = models.CharField(max_length=20, verbose_name='Ник')
    slug = models.SlugField(max_length=20, unique=True, db_index=True, verbose_name='URL')
    name = models.CharField(max_length=50, verbose_name='Имя')
    photo = models.ImageField(upload_to='photo/%Y/%m/%d/', verbose_name='Фото', blank=True)
    comment = models.CharField(max_length=255, verbose_name='Комментарии')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время обновления')
    comm = models.ForeignKey('Community', on_delete=models.PROTECT, null=True, verbose_name='Сообщества')

    def get_absolute_url(self):
        return reverse('player', kwargs={'player_slug': self.slug})

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Игрок'
        verbose_name_plural = 'Игроки'
        ordering =['time_create', 'username']


class Community(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Название')
    slug = models.SlugField(max_length=20, unique=True, db_index=True, verbose_name='URL')

    def get_absolute_url(self):
        return reverse('community', kwargs={'community_slug': self.slug})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сообщество'
        verbose_name_plural = 'Сообщества'
        ordering =['name']