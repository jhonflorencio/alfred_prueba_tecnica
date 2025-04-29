from abc import ABC, abstractmethod
from django.shortcuts import get_object_or_404

from apps.api.models.driver import DriverModel


class IDriverModelRepository(ABC):
    @abstractmethod
    def create(self):
        pass
    
    @abstractmethod
    def get_detail(self):
        pass

    @abstractmethod
    def set_update_by_pk(self):
        pass
    
    @abstractmethod
    def get_all_is_available(self):
        pass


class DriverModelRepository(IDriverModelRepository):

    def __init__(self):
        self._model = DriverModel

    def create(self, data: dict) -> DriverModel:
        return self._model.objects.create(**data)

    def get_detail(self, pk: int) -> DriverModel:
        return get_object_or_404(self._model, pk=pk)

    def set_update_by_pk(self, pk: int, data: dict) -> DriverModel:
        self._model.objects.filter(pk=pk).update(**data)
        return self.get_detail(pk)

    def get_all_is_available(self) -> list[DriverModel]:
        return self._model.objects.filter(is_available=True).all()