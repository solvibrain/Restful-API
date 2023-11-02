from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200,default=None)
    price = models.DecimalField(max_digits=5, decimal_places=2,default=99.99)
    description = models.TextField(max_length=100,default=None)