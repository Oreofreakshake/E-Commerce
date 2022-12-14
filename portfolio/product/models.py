from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inStock = models.BooleanField(default=False)
