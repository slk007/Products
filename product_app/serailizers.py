from rest_framework import serializers

from .models import Product

class ProductSerailizer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('name', 'price', 'avg_rating')
