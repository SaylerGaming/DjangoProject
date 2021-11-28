from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import BooleanField, CharField, DurationField, PositiveIntegerField
from django.db.models.fields.related import ForeignKey
from django.db.models.fields.related_descriptors import create_forward_many_to_many_manager

from companies.models import Company
from users.models import Profile

# Create your models here.

class RecomendedContent(models.Model):
    company = models.ForeignKey(Company, on_delete=CASCADE, null=True, blank=True)
    duration = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    def  __str__(self):
        return self.company

class Review(models.Model):
    profile = models.ForeignKey(Profile, on_delete=CASCADE, null=True, blank=True)
    stars = models.PositiveIntegerField()
    company = models.ForeignKey(Company, on_delete=CASCADE, null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def  __str__(self):
        return self.profile

class Reserve(models.Model):
    company = ForeignKey(Company, on_delete=CASCADE, null=True, blank=True)
    name = CharField(max_length=255)
    price = PositiveIntegerField(null=True, blank=True)
    is_availabe = BooleanField(default=1)

class UsedReserve(models.Model):
    profile = ForeignKey(Profile, on_delete=CASCADE, null=True, blank=True)
    reserve = ForeignKey(Reserve, on_delete=CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def  __str__(self):
        return self.created_at
