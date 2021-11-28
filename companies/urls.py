from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('company/<str:slug>', views.company, name='company'),
    path('companies', views.companies, name='companies'),

    path('your-company/', views.companyIndex, name='companyIndex'),
    path('your-company/advertise', views.companyAdvertise, name='companyAdvertise'),
    path('your-company/categories', views.companyCategories, name='companyCategories'),

    path('your-company/category/create', views.categoryCreate, name='categoryCreate'),
    path('your-company/category/update/<str:id>', views.categoryUpdate, name='categoryUpdate'),
    path('your-company/category/delete/<str:id>', views.categoryDelete, name='categoryDelete'),
    
    path('your-company/product/create/', views.createProduct, name='createProduct'),
    path('your-company/product/update/<int:id>/', views.updateProduct, name='updateProduct'),
    path('your-company/product/delete/<int:id>/', views.deleteProduct, name='deleteProduct'),
]