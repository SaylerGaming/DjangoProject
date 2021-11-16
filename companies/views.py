from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Guarantee, Company, Category, Product
from .forms import ProductForm

def index(request):
    guarantees = Guarantee.objects.all()
    companies = Company.objects.all()
    return render(request, 'companies/index.html', {'guarantees': guarantees, 'companies': companies})

def company(request, slug):
    company = Company.objects.get(slug=slug)
    return render(request, )

def companies(request):
    companies = Company.objects.all()
    return render(request, 'companies/companies.html', {'companies':companies, 'numbers':[1,2,3,4,5]})


def createProduct(request):
    form = ProductForm()

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index') 
    context = {'form': form}
    return render(request, 'companies/product_form.html', context)

def updateProduct(request, id):
    product = Product.objects.get(id=id)
    form = ProductForm(instance=product)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('index') 
    context = {'form': form}
    return render(request, 'companies/product_form.html', context)

def deleteProduct(request, id):
    product = Product.objects.get(id=id)
    if request.method == 'POST':
        product.delete()
        return redirect('index')
    context = {'object':product}
    return render(request, 'admin/deleteObject.html', context)