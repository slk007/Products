from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    avg_rating = models.IntegerField(default=0)
    rating_score = [0,0,0,0,0,0]

    def __str__(self):
        return str(self.name)


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    reviewer_name = models.CharField(max_length=30, default="Anonymous")
    review_string = models.CharField(max_length=200)
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    evaluated = models.BooleanField(default='False')
    
    def __str__(self):
        return str(self.review_string)
    