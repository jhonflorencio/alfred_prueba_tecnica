from rest_framework import serializers

from apps.api.models.address import AddressModel
from apps.api.models.driver import DriverModel
from apps.api.models.service import ServiceModel


class ServiceModelCreateSerializer(serializers.ModelSerializer):
    address_model_id = serializers.PrimaryKeyRelatedField(
        source="address_model",
        queryset=AddressModel.objects.only("id"),
        required=True,
    )
    driver_model_id = serializers.PrimaryKeyRelatedField(
        source="driver_model",
        queryset=DriverModel.objects.only("id"),
        required=False,
    )
    class Meta:
        model = ServiceModel
        fields = ["driver_model_id", "address_model_id", "estimated_time", "estimated_distance"]

