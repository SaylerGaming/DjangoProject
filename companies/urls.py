from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('company/<str:slug>', views.company, name='company'),
]