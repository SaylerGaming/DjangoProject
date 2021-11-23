from django.contrib.messages.api import error
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.urls import conf
from .forms import CustomUserCreationForm, CompanyForm
from companies.models import Company
from .models import Profile

def loginUser(request):

    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Пользователя с таким никнеймом не существует')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Никнейм или пароль введен неверно')

    form = CustomUserCreationForm()
    context = {'form': form}
    return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    messages.error(request, 'Puf!')
    return redirect('loginUser')

def registerUser(request):
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Пользователь создан!')
            login(request, user)
            return redirect('index')
        else:
            messages.error('При регистрации произошла ошибка')
    context = {'form': form}
    return render(request, 'register.html', context)

def userProfile(request):
    return render(request, 'profile.html')

def createCompany(request):
    form = CompanyForm()
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            company = form.save()
            profile = Profile.objects.get(user_id=request.user.id)
            profile.company_id = company.id
            profile.save()
            return redirect('createCompany') 
    return render(request, 'createCompany.html', {'form': form})