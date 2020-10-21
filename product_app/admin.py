from django.contrib import admin
from .models import Product, Review, Rating


# Register your models here.
class ReviewInline(admin.TabularInline):
    model = Review

class RatingInline(admin.StackedInline):
    model = Rating

class ProductAdmin(admin.ModelAdmin):
    model = Product
    inlines = [ReviewInline, RatingInline]

admin.site.register(Product, ProductAdmin)
# admin.site.register(Rating)