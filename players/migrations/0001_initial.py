# Generated by Django 4.2.1 on 2023-05-14 09:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Название')),
                ('slug', models.SlugField(max_length=20, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Сообщество',
                'verbose_name_plural': 'Сообщества',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Players',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, verbose_name='Ник')),
                ('slug', models.SlugField(max_length=20, unique=True, verbose_name='URL')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('photo', models.ImageField(blank=True, upload_to='photo/%Y/%m/%d/', verbose_name='Фото')),
                ('comment', models.CharField(max_length=255, verbose_name='Комментарии')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Время обновления')),
                ('comm', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='players.community', verbose_name='Сообщества')),
            ],
            options={
                'verbose_name': 'Игрок',
                'verbose_name_plural': 'Игроки',
                'ordering': ['time_create', 'username'],
            },
        ),
    ]
