from django.db import models


# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'


class Model(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name} {self.brand}'


class Car(models.Model):
    class Situation(models.TextChoices):
        WORKSHOP = "Workshop", "Workshop"
        RENTED = "Rented", "Rented"
        AVAILABLE = "Available", "Available"

    class Color(models.TextChoices):
        RED = "Red", "Red"
        GREEN = "Green", "Green"
        BLUE = "Blue", "Blue"

    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    plate = models.IntegerField()
    situation = models.TextField(choices=Situation.choices, default=Situation.AVAILABLE, max_length=20)
    color = models.TextField(choices=Color.choices, default=Color.RED, max_length=20)
    km = models.FloatField(null=True, default=0)
    price = models.FloatField(null=True)

    def __str__(self):
        return f'{self.id} {self.plate} {self.model} {self.situation} {self.color} {self.km} {self.price}'

class Tourist(models.Model):
    name = models.CharField(max_length=50)
    birth_date = models.DateField()
    dni = models.CharField(max_length=20)
    passport = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name} {self.birth_date} {self.dni} {self.passport}'