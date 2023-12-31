from django.db import models


class Review(models.Model):
    text = models.TextField()

    product = models.ForeignKey('Product', on_delete=models.CASCADE)


class Category(models.Model):
    name = models.CharField(max_length=50)


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    img = models.ImageField(null=True)

    Categoryes = models.ManyToManyField(Category)
