from django.db import models
import uuid

# Create your models here.

class Guarantee(models.Model):
    image = models.CharField(max_length=255, null=True)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    def  __str__(self):
        return self.text