from .models import Profile
from companies.models import Company
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete

def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username = user.username,
            email = user.email,
        )

def deleteUser(sender, instance, **kwargs):
    user = instance.user
    user.delete()

post_save.connect(createProfile, sender=User)

post_delete.connect(deleteUser, sender=Profile)