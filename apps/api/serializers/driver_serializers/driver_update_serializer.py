from rest_framework import serializers

from apps.api.models.driver import DriverModel


class DriverModelUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverModel
        fields = ["id", "name", "email", "latitude", "longitude", "phone"]
