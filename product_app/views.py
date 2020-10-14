from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView, CreateView
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

class CreateReview(CreateView):
    model = Review
    fields = ['product', 'reviewer_name', 'review_string', 'rating']

    success_url = reverse_lazy('list')