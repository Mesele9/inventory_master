from django.contrib import admin
from .models import Item, Category, UserProfile

admin.site.register(Item)
admin.site.register(Category)
admin.site.register(UserProfile)