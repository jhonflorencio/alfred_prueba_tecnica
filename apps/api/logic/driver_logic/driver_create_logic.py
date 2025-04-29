from abc import ABC, abstractmethod
from rest_framework.serializers import Serializer
from rest_framework import status
from rest_framework.response import Response


from apps.api.repository.driver_repository.driver_repository import (
    DriverModelRepository,
)


class IDriverModelCreateLogic(ABC):

    @abstractmethod
    def process(self):
        pass


class DriverModelCreateLogic(IDriverModelCreateLogic):

    def __init__(self, serializer: Serializer, repository: DriverModelRepository):
        self._repository = repository
        self._serializer = serializer

    def process(self) -> Response:
        self._serializer.is_valid(raise_exception=True)
        driver_data = self._serializer.validated_data
        instance = self._repository.create(driver_data)
        return Response({"id": instance.id}, status=status.HTTP_201_CREATED)
