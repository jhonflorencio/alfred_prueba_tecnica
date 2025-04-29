from abc import ABC, abstractmethod
from django.shortcuts import get_object_or_404

from apps.api.models.driver import DriverModel
from apps.api.models.service import ServiceModel


class IServiceModelRepository(ABC):
    @abstractmethod
    def create(self):
        pass
    
    @abstractmethod
    def get_detail(self):
        pass

    @abstractmethod
    def set_update_by_pk(self):
        pass

    

class ServiceModelRepository(IServiceModelRepository):

    def __init__(self):
        self._model = ServiceModel
        self._driver_model = DriverModel

    def create(self, data: dict) -> ServiceModel:
        return self._model.objects.create(**data)

    def get_detail(self, pk: int) -> ServiceModel:
        return get_object_or_404(self._model, pk=pk)

    def set_update_by_pk(self, pk: int, data: dict) -> ServiceModel:
        self._model.objects.filter(pk=pk).update(**data)
        return self.get_detail(pk)
    