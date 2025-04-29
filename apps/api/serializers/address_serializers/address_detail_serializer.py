from rest_framework import serializers

from apps.api.models.address import AddressModel


class AddressModelDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = AddressModel
        fields = ["id", "name", "reference", "client_model_id", "latitude", "longitude"]
