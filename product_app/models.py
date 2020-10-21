from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    avg_rating = models.IntegerField(default=0, editable=False)

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
    

class Rating(models.Model):

    product = models.OneToOneField(Product, on_delete=models.CASCADE, primary_key=True)
    zero_star = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    one_star = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    two_star = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    three_star = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    four_star = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    five_star = models.IntegerField(default=0, validators=[MinValueValidator(0)])

    def __str__(self):
        return str(f'{self.zero_star} {self.one_star} {self.two_star} {self.three_star} {self.four_star} {self.five_star}')
    
