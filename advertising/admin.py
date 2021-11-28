from django.contrib import admin
from .models import RecomendedContent, Review, Reserve, UsedReserve

admin.site.register(RecomendedContent)
admin.site.register(Review)
admin.site.register(Reserve)
admin.site.register(UsedReserve)
