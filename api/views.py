from django.shortcuts import render
from rest_framework import viewsets

from api.serializers import TouristaSerializer
from rentcar.models import Tourist


# Create your views here.
class TouristViewSet(viewsets.ModelViewSet):
    queryset = Tourist.objects.all()
    serializer_class = TouristaSerializer