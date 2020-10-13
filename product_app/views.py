from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import ListView, DetailView
from .models import Product, Review

# Create your views here.

def home(request):

    return render(request, 'product_app/home.html')

class ProductListView(ListView):
    model = Product

class ProductDetailView(DetailView):
    model = Product

class ReviewListView(ListView):
    model = Review

