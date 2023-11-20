from django import forms
from rentcar.models import Brand, Tourist
from rentcar.models import Car
from rentcar.models import Model


class BrandCreateForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['name']


# class ModelCreateForm(forms.ModelForm):
#     class Meta:
#         model = Model
#         fields = ['name', 'brand']


class CarCreateForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['model', 'plate', 'situation', 'color', 'km', 'price']


class BrandUpdateForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['name']


class ModelUpdateForm(forms.ModelForm):
    class Meta:
        model = Model
        fields = ["name"]


class ModelCreateForm(forms.ModelForm):
    class Meta:
        model = Model
        fields = ["name","brand"]


class TouristForm(forms.ModelForm):
    class Meta:
        model = Tourist
        fields = '__all__'


class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = '__all__'