from django.shortcuts import render
from django.http import HttpResponse
from .models import Guarantee

def index(request):
    guarantees = Guarantee.objects.all()
    return render(request, 'companies/index1.html', {'guarantees': guarantees})

def company(request, pk):
    return HttpResponse('One company ' + pk) 
