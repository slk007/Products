from django.urls import path

from .views import ProductListView, ProductDetailView, home

urlpatterns = [
    path('', home, name="home"),
    path('product/', ProductListView.as_view(), name="list"),
    path('product/<int:pk>/', ProductDetailView.as_view(), name="detail"),
    # path('product/<int:pk>/reviews', name="review_list"),
]