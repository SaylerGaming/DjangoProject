from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Guarantee, Company, Category, Product
from .forms import ProductForm
from users.models import Profile

def index(request):
    guarantees = Guarantee.objects.all()
    companies = Company.objects.all()
    return render(request, 'companies/index.html', {'guarantees': guarantees, 'companies': companies})

@login_required(login_url='loginUser')
def company(request, slug):
    company = Company.objects.get(slug=slug)
    return render(request, 'companies/company.html', {'company': company})

def companies(request):
    companies = Company.objects.all()
    return render(request, 'companies/companies.html', {'companies':companies, 'numbers':[1,2,3,4,5]})


def companyIndex(request):
    user = Profile.objects.get(username = request.user.username)
    company = user.company
    products = Product.objects.filter(company_id=company.id)
    context = {'user': user, 'company': company, 'products': products}
    return render(request, 'your-company/index.html', context)

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
    Product.objects.get(id=id).delete()
    return redirect('index')