from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.
class Creator(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Technique(models.Model):
    name = models.CharField(max_length=32)
    creators = models.ManyToManyField("Creator")

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    creator = models.ForeignKey("Creator", on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f'{self.creator} {self}'


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    products = models.ManyToManyField(Product, through="OrderProduct")


class OrderProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField()


class Type(models.Model):
    name = models.CharField(max_length=100)
    creators = models.ManyToManyField("Creator")
    techniques = models.ManyToManyField("Technique")

    def __str__(self):
        return f'{self.name}'
