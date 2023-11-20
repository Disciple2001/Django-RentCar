from rest_framework import serializers

from rentcar.models import Tourist


class TouristaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tourist
        fields = '__all__'