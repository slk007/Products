from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView, CreateView

from .models import Product, Review
from .serailizers import ProductSerailizer

from rest_framework import viewsets

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


def evaluation(request):

    products = Product.objects.all()
    for product in products:

        product_rating_list = [0,0,0,0,0,0]

        for review in product.review_set.all():
            rating = review.rating
            product_rating_list[rating] += 1
            review.evaluated = True
            review.save()

        average = 0
        for i in range(0,6):
            average += i*product_rating_list[i]
        average = average/sum(product_rating_list)

        product.avg_rating = int(average)
        product.rating_score = product_rating_list
        product.save()

        print("in db:")
        print(product.avg_rating)
        print(product.rating_score)

    return render(request, 'product_app/evaluated.html')


# viewset for serializer

class ProductViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all().order_by('name')
    serializer_class = ProductSerailizer