import pytest

from apps.api.models import DriverModel

from apps.api.serializers.driver_serializers.driver_create_serializer import DriverCreateSerializer

@pytest.mark.django_db
class TestDriverSerializer:
    def test_valid_data(self):
        """Valida la data del serializador si es correcta"""
        data = {
            "name": "John Doe",
            "email": "john.doe@example.com",
            "latitude": 40.7128,
            "longitude": -74.0060,
            "phone": "123456789"
        }
        serializer = DriverCreateSerializer(data=data)
        assert serializer.is_valid(), serializer.errors
        assert serializer.validated_data == {
            "name": "John Doe",
            "email": "john.doe@example.com",
            "latitude": 40.7128,
            "longitude": -74.0060,
            "phone": "123456789"
        }

    def test_missing_required_field(self):
        """Test que el serializador falla si falta un campo requerido."""
        data = {
            "name": "John Doe",
            # email falta
            "latitude": 40.7128,
            "longitude": -74.0060,
            "phone": "+1234567890"
        }
        serializer = DriverSerializer(data=data)
        assert not serializer.is_valid()
        assert "email" in serializer.errors
        assert serializer.errors["email"][0].code == "required"

    def test_invalid_email(self):
        """Test que el serializador falla si el email es invalido."""
        data = {
            "name": "John Doe",
            "email": "invalid-email",
            "latitude": 40.7128,
            "longitude": -74.0060,
            "phone": "+1234567890"
        }
        serializer = DriverSerializer(data=data)
        assert not serializer.is_valid()
        assert "email" in serializer.errors
        assert serializer.errors["email"][0].code == "invalid"

    def test_serialize_instance(self):
        """Test que verifica que el serializador devuelve una instancia de DriverModel correctamente
        """
        
        driver = DriverModel.objects.create(
            name="Jane Doe",
            email="jane.doe@example.com",
            latitude=34.0522,
            longitude=-118.2437,
            phone="987654321"
        )
        serializer = DriverSerializer(instance=driver)
        expected_data = {
            "name": "Jane Doe",
            "email": "jane.doe@example.com",
            "latitude": 34.0522,
            "longitude": -118.2437,
            "phone": "987654321"
        }
        assert serializer.data == expected_data    