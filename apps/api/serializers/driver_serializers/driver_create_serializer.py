from rest_framework import serializers

from apps.api.models.driver import DriverModel



class DriverModelCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverModel
        fields = ["name", "email", "latitude", "longitude", "phone"]

