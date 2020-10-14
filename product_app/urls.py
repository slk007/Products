from django.urls import path

from .views import home, evaluation , ProductListView, ProductDetailView, CreateReview

urlpatterns = [

    path('', home, name="home"),

    path('product/', ProductListView.as_view(), name="list"),
    path('product/<int:pk>/', ProductDetailView.as_view(), name="detail"),
    path('product/<int:pk>/add_review/', CreateReview.as_view(), name="add_review"),
    path('evaluation', evaluation, name="evaluation"),
    
]