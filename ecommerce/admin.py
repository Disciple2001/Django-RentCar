from django.contrib import admin

from ecommerce.models import Category, Product, Order, Coupon, Customer, Status

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Coupon)
admin.site.register(Customer)
admin.site.register(Status)

