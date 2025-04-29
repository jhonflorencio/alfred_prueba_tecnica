from abc import ABC, abstractmethod
from rest_framework.serializers import Serializer
from rest_framework import status
from rest_framework.response import Response

from apps.api.repository.driver_repository.driver_repository import (
    DriverModelRepository,
)


class IDriverModelUpdateLogic(ABC):

    @abstractmethod
    def process(self):
        pass


class DriverModelUpdateLogic(IDriverModelUpdateLogic):

    def __init__(
        self,
        pk: int,
        data: dict,
        serializer: Serializer,
        repository: DriverModelRepository,
    ):
        self._pk = pk
        self._data = data
        self._repository = repository
        self._serializer = serializer

    def process(self) -> Response:
        instance = self._repository.get_detail(self._pk)
        serializer = self._serializer(instance, data=self._data, partial=True)
        serializer.is_valid(raise_exception=True)
        instance = self._repository.set_update_by_pk(
            self._pk, serializer.validated_data
        )
        updated_serializer = self._serializer(instance)
        return Response({"data": updated_serializer.data}, status=status.HTTP_200_OK)
