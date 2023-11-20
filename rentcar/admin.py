from django.contrib import admin
from .models import Car
from .models import Brand
from .models import Model
from .models import Tourist


# Register your models here.
class CarAdmin(admin.ModelAdmin):
    list_display = ("id", "plate", "model", "situation", "color", "km", "price")


class TouristAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


class BrandAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


class ModelAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "brand")


admin.site.register(Car, CarAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Model, ModelAdmin)
admin.site.register(Tourist, TouristAdmin)
