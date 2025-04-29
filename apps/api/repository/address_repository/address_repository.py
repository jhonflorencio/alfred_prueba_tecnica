from abc import ABC, abstractmethod
from django.shortcuts import get_object_or_404

from apps.api.models.address import AddressModel


class IAddressModelRepository(ABC):
    @abstractmethod
    def create(self):
        pass
    
    @abstractmethod
    def get_detail(self):
        pass

    @abstractmethod
    def set_update_by_pk(self):
        pass


class AddressModelRepository(IAddressModelRepository):

    def __init__(self):
        self._model = AddressModel

    def create(self, data: dict) -> AddressModel:
        return self._model.objects.create(**data)

    def get_detail(self, pk: int) -> AddressModel:
        return get_object_or_404(self._model, pk=pk)

    def set_update_by_pk(self, pk: int, data: dict) -> AddressModel:
        self._model.objects.filter(pk=pk).update(**data)
        return self.get_detail(pk)
