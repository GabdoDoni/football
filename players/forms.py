from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import *

class AddPlayerForm(forms.ModelForm):
    # username = forms.CharField(max_length=20, label='Ник')
    # slug = forms.SlugField(max_length=20, label='URL')
    # name = forms.CharField(max_length=50, label='Имя')
    # comment = forms.CharField(max_length=255, label='Комментарии')
    # comm = forms.ModelChoiceField(queryset=Community.objects.all(), label='Сообщества', empty_label='Не выбрана')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['comm'].empty_label = 'Не выбрана'

    class Meta:
        model = Players
        fields = ['username', 'slug', 'name', 'comment', 'photo', 'comm']
        widgets ={
            'username': forms.TextInput(attrs={'class': 'form-input'}),
            'comment': forms.TextInput(attrs={'class': 'form-input'}),
        }


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

