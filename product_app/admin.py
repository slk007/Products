from django.contrib import admin
from .models import Product, Review


# Register your models here.
class ReviewInline(admin.TabularInline):
    model = Review

class ProductAdmin(admin.ModelAdmin):
    model = Product
    inlines = [ReviewInline]

admin.site.register(Product, ProductAdmin)