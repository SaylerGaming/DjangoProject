from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('company/<str:slug>', views.company, name='company'),
    path('companies', views.companies, name='companies'),

    path('super-admin/company/<str:slug>', views.adminIndex, name='adminIndex'),
    path('product/create/', views.createProduct, name='createProduct'),
    path('product/update/<int:id>/', views.updateProduct, name='updateProduct'),
    path('product/delete/<int:id>/', views.deleteProduct, name='deleteProduct'),
]