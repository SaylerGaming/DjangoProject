from django.core.checks import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Guarantee, Company, Category, Product
from .forms import ProductForm
from users.models import Profile
from advertising.models import RecomendedContent, Review
from django.contrib import messages
from advertising.models import RecomendedContent, Review
from datetime import datetime, timedelta

def index(request):
    guarantees = Guarantee.objects.all()
    guarantees_count = Guarantee.objects.all().count()
    guarantees_count = list(range(0, guarantees_count))
    guarantees_count_2 = guarantees_count
    companies = Company.objects.all()
    advertise = RecomendedContent.objects.all()
    return render(request, 'companies/index.html', {'guarantees': guarantees, 'companies': companies, 'advertise':advertise, 'guarantees_count':guarantees_count, 'guarantees_count_2': guarantees_count_2})

def company(request, slug):
    company = Company.objects.get(slug=slug)
    products = Product.objects.filter(company_id=company.id)
    reviews = Review.objects.filter(company=company)
    context = {'numbers':[1,2,3,4,5], 'company': company, 'products': products, 'reviews':reviews}
    return render(request, 'companies/company.html', context)

def companies(request):
    companies = Company.objects.filter(is_confirmed=1)
    return render(request, 'companies/companies.html', {'companies':companies, 'numbers':[1,2,3,4,5]})


def companyIndex(request):
    user = Profile.objects.get(user_id = request.user.id)
    company = user.company
    products = Product.objects.filter(company_id=company.id)
    context = {'user': user, 'company': company, 'products': products}
    return render(request, 'your-company/index.html', context)

def companyAdvertise(request):
    user = Profile.objects.get(user_id = request.user.id)
    company = user.company
    try:
        ad = RecomendedContent.objects.get(company=company)
    except:
        ad = None
    if ad is not None:
        ad.created_at = datetime.date(ad.created_at)
    context = {'user': user, 'company': company, 'ad':ad}
    if request.method == 'POST':
        duration = request.POST['duration']
        if duration == 'custom':
            duration = request.POST['days']
        RecomendedContent.objects.create(company = company, duration = duration)
        messages.success(request, 'Реклама заказана!')
        return redirect('companyIndex')
    return render(request, 'your-company/advertise.html', context)

def createProduct(request):
    form = ProductForm()
    page = {'title':'Созать Товар', 'btn':'Создать'}
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            user = Profile.objects.get(user_id=request.user.id)
            product.company_id = user.company_id
            product.save()
            return redirect('index') 
    context = {'form': form, 'page':page}
    return render(request, 'your-company/product_form.html', context)

@login_required(login_url='loginUser')
def updateProduct(request, id):
    product = Product.objects.get(id=id)
    page = {'title':'Изменить Товар', 'btn':'Изменить'}
    form = ProductForm(instance=product)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('companyIndex') 
    context = {'form': form, 'page':page}
    return render(request, 'your-company/product_form.html', context)

def deleteProduct(request, id):
    Product.objects.get(id=id).delete()
    return redirect('companyIndex')

def companyCategories(request):
    categories = Category.objects.all()
    return render(request, 'your-company/categories.html', {'categories':categories})

def categoryCreate(request):
    if request.method == 'POST':
        Category.objects.create(name = request.POST['name'], slug = request.POST['slug'])
    return redirect('companyCategories')

def categoryUpdate(request, id):
    category = Category.objects.get(id=id)
    if request.method == 'POST':
        slug = request.POST['slug'].lower()
        slug = list(slug)
        category_slug = ''
        for i in slug:
            if i == ' ':
                category_slug = category_slug + '_'
            else:
                category_slug = category_slug + i
        try:
            slug_check = Category.objects.get(slug=category_slug)
        except:
            slug_check = None
        if slug_check is not None and slug_check != category:
            messages.error(request, 'Данная ссылка уже используется')
            return redirect('companyCategories')
        category.name = request.POST['name']
        category.slug = category_slug
        category.save()
        return redirect('companyCategories')
    return render(request, 'your-company/categoryUpdate.html', {'category': category})
    
def categoryDelete(request, id):
    Category.objects.get(id=id).delete()
    messages.success(request, 'категория удалена')
    return redirect('companyCategories')

def companyReview(request, slug):
    company = Company.objects.get(slug=slug)
    reviews = Review.objects.filter(company=company)
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id = request.user.id)
        try:
            userReview = Review.objects.get(company=company, profile=profile)
        except:
            userReview = None
    if(request.method == 'POST'):
        profile = Profile.objects.get(user_id = request.user.id)
        review = Review.objects.create(profile=profile, stars=request.POST['stars'], company=company, text=request.POST['comment'])
        companyRating = 0
        ReviewCount = 0
        for item in reviews:
            companyRating += item.stars
            ReviewCount += 1
        companyRating = (companyRating + int(request.POST['stars'])) / (ReviewCount + 1) 
        company.rating = companyRating
        company.save()
        return redirect('companyReview', slug)
    context = {'company':company, 'reviews':reviews, 'userReview':userReview, 'numbers':[1,2,3,4,5]}
    return render(request, 'companies/review.html', context)