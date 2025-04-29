from abc import ABC, abstractmethod
from rest_framework.serializers import Serializer
from rest_framework import status
from rest_framework.response import Response

from apps.api.repository.address_repository.address_repository import (
    AddressModelRepository,
)


class IAddressModelDetailLogic(ABC):

    @abstractmethod
    def process(self):
        pass


class AddressModelDetailLogic(IAddressModelDetailLogic):

    def __init__(
        self, pk: int, serializer: Serializer, repository: AddressModelRepository
    ):
        self._pk = pk
        self._repository = repository
        self._serializer = serializer

    def process(self) -> Response:
        instance = self._repository.get_detail(self._pk)
        serializer = self._serializer(instance=instance)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)
