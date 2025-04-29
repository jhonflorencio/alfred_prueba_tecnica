from abc import ABC, abstractmethod
from rest_framework.serializers import Serializer
from rest_framework import status
from rest_framework.response import Response


from apps.api.repository.address_repository.address_repository import (
    AddressModelRepository
)


class IAddressModelCreateLogic(ABC):

    @abstractmethod
    def process(self):
        pass


class AddressModelCreateLogic(IAddressModelCreateLogic):

    def __init__(self, serializer: Serializer, repository: AddressModelRepository):
        self._repository = repository
        self._serializer = serializer

    def process(self) -> Response:
        self._serializer.is_valid(raise_exception=True)
        driver_data = self._serializer.validated_data
        instance = self._repository.create(driver_data)
        return Response({"id": instance.id}, status=status.HTTP_201_CREATED)
