from django.urls import path, include

from rest_framework import routers

from .views import home, evaluation , ProductListView, ProductDetailView, CreateReview, ProductViewSet

router = routers.DefaultRouter()
router.register('product', ProductViewSet)

urlpatterns = [

    path('', home, name="home"),

    path('product/', ProductListView.as_view(), name="list"),
    path('product/<int:pk>/', ProductDetailView.as_view(), name="detail"),
    path('product/<int:pk>/add_review/', CreateReview.as_view(), name="add_review"),
    path('evaluation', evaluation, name="evaluation"),

    path('api/', include(router.urls))
    
]