from django.db import models
import uuid

from django.db.models.fields.related import ForeignKey

# Create your models here.

class Guarantee(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to='guarantees/', default='guarantees/default.png')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    def  __str__(self):
        return self.text
    
class Company(models.Model):
    name = models.CharField(max_length=255)
    rating = models.SmallIntegerField(null=True)
    description = models.TextField(null=True)
    logo = models.ImageField(null=True, blank=True, upload_to='companies/logo/', default='companies/logo/default.png')
    logo_min = models.ImageField(null=True, blank=True, upload_to='companies/logo_min/', default='companies/logo_min/default.png')
    categories = models.ManyToManyField('Category', blank=True)
    is_confirmed = models.BooleanField(default=0)
    slug = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def  __str__(self):
        return self.name
class Category(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.CharField(max_length=255, unique=True)
    def  __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(null=True, blank=True, upload_to='companies/products/', default='companies/products/default.png')
    description = models.TextField(null=True)
    price = models.PositiveIntegerField()
    new_price = models.PositiveIntegerField(null=True)
    category = ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    company = ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def  __str__(self):
        return self.name
