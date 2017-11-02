from django.contrib import admin

# Register your models here.

from .models import FoodCalorie

admin.site.register(FoodCalorie)