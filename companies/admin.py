from django.contrib import admin

# Register your models here.
from .models import Guarantee, Company, Category, Product

admin.site.register(Guarantee)
admin.site.register(Company)
admin.site.register(Category)
admin.site.register(Product)