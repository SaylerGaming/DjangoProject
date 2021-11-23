from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from companies.models import Company, Product

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    username = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    profile_image = models.ImageField(null=True, blank=True, upload_to='profiles/', default='profiles/default.png')
    created_at = models.DateTimeField(auto_now_add=True)
    company = models.OneToOneField(Company, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return str(self.user.username)

class Favorite(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)