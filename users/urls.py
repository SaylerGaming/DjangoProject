from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginUser, name='loginUser'),
    path('register/', views.registerUser, name='registerUser'),
    path('logout/', views.logoutUser, name='logoutUser'),
    path('user/', views.userProfile, name='userProfile'),
    path('create-company/', views.createCompany, name='createCompany')
]