from abc import ABC, abstractmethod
from rest_framework.serializers import Serializer
from rest_framework import status
from rest_framework.response import Response


from apps.api.repository.driver_repository.driver_repository import (
    DriverModelRepository,
)


class IDriverModelDetailLogic(ABC):

    @abstractmethod
    def process(self):
        pass


class DriverModelDetailLogic(IDriverModelDetailLogic):

    def __init__(
        self, pk: int, serializer: Serializer, repository: DriverModelRepository
    ):
        self._pk = pk
        self._repository = repository
        self._serializer = serializer

    def process(self) -> Response:
        instance = self._repository.get_detail(self._pk)
        serializer = self._serializer(instance=instance)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)
