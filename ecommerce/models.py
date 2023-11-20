from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models


class Customer(User):
    # birth_date = models.DateField(default=None, blank=True, null=True)
    address = models.TextField(default=None, blank=True, null=True)

class Category(models.Model):
    name = models.CharField(max_length=50)


class Coupon(models.Model):
    code = models.CharField(max_length=10)
    quantity = models.IntegerField()
    discount = models.DecimalField(max_digits=2, decimal_places=2)
    init_date = models.DateField()
    expiration_date = models.DateField()


class Product(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=2, decimal_places=2)
    quantity = models.IntegerField()
    discount = models.DecimalField(max_digits=2, decimal_places=2)
    photo = models.ImageField(upload_to='products/')
    categories = models.ManyToManyField(Category)


class Order(models.Model):
    customer = models.ForeignKey(Customer, blank=True, null=True, default=None, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=2, decimal_places=2)
    coupons = models.ManyToManyField(Coupon)
    address = models.CharField(max_length=255)
    email = models.EmailField()
    destination_address = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Status(models.Model):
    name = models.CharField(max_length=50)


class OrderStatus(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)


class ProductOrder(models.Model):
    price = models.DecimalField(max_digits=2, decimal_places=2)
    quantity = models.IntegerField()
    discount = models.DecimalField(max_digits=2, decimal_places=2)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
