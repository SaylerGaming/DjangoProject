from django import forms
from django.forms import ModelForm, widgets
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from companies.models import Company

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Никнейм'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'имя'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Почта'}))
    password1 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Пароль', 'type':'password'}))
    password2 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Подтверждение пароля', 'type':'password'}))
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']

class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'description', 'logo', 'logo_min', 'slug']