from django.contrib import admin

from .models import category, Product
# Register your models here.

admin.site.register(Product)
admin.site.register(category)