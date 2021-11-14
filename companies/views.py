from django.shortcuts import render
from django.http import HttpResponse
from .models import Guarantee, Company, Category

def index(request):
    guarantees = Guarantee.objects.all()
    companies = Company.objects.all()
    return render(request, 'companies/index.html', {'guarantees': guarantees, 'companies': companies})

def company(request, slug):
    company = Company.objects.get(slug=slug)
    return HttpResponse('One company ' + company.name)


