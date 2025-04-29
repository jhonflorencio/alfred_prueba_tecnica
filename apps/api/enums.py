from enum import Enum

class ServiceStatus(Enum):
    PENDING = ("pending", "Pendiente")
    IN_TRANSIT = ("in_transit", "En Tránsito")
    DELIVERED = ("delivered", "Entregado")
    CANCELLED = ("cancelled", "Cancelado")

    @property
    def value(self):
        return self._value_[0]

    @property
    def display(self):
        return self._value_[1]

    @classmethod
    def choices(cls):
        return [(status.value, status.display) for status in cls]