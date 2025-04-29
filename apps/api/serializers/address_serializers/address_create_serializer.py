from rest_framework import serializers

from apps.api.models.address import AddressModel
from apps.api.models.client import ClientModel


class AddressModelCreateSerializer(serializers.ModelSerializer):
    client_model_id = serializers.PrimaryKeyRelatedField(
        source="client_model",
        queryset=ClientModel.objects.only("id"),
        required=True,
    )

    class Meta:
        model = AddressModel
        fields = ["name", "reference", "client_model_id", "latitude", "longitude"]
