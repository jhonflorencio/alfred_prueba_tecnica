import requests
from dotenv import dotenv_values
from decimal import Decimal
from abc import ABC, abstractmethod
from rest_framework.serializers import Serializer
from rest_framework import status
from rest_framework.response import Response

from apps.api.repository.driver_repository.driver_repository import (
    DriverModelRepository,
)
from apps.api.repository.service_repository.service_repository import (
    ServiceModelRepository,
)
from alfred.common.distance import calculate_distance

env = dotenv_values()


class IServiceModelCreateLogic(ABC):

    @abstractmethod
    def process(self):
        pass


class ServiceModelCreateLogic(IServiceModelCreateLogic):

    def __init__(self, serializer: Serializer, repository: ServiceModelRepository):
        self._repository = repository
        self._serializer = serializer
        self._driver_model_repository = DriverModelRepository()

    def process(self) -> Response:
        self._serializer.is_valid(raise_exception=True)
        service_data = self._serializer.validated_data
        service_data.update(self._get_field_empty())
        instance = self._repository.create(service_data)
        return Response({"id": instance.id}, status=status.HTTP_201_CREATED)

    def _get_field_empty(self) -> dict:
        latitude_client, longitude_client = self._get_coordenates_address_client()
        estimated_distance_and_driver = self._get_estimated_distance_and_driver()
        driver_model_id = estimated_distance_and_driver[0]
        estimated_distance = estimated_distance_and_driver[1]
        latitude_driver, longitude_driver = self._get_coordinates_driver(
            driver_model_id
        )
        estimated_time = self._get_estimated_time(
            (longitude_driver, latitude_driver), (longitude_client, latitude_client)
        )

        return {
            "estimated_distance": estimated_distance,
            "driver_model_id": driver_model_id,
            "estimated_time": estimated_time,
        }

    def _get_estimated_distance_and_driver(self) -> list[int | Decimal]:
        latitud_client, longitud_client = self._get_coordenates_address_client()
        return self._get_estimated_distance_min(latitud_client, longitud_client)

    def _get_coordenates_address_client(self) -> tuple[Decimal, Decimal]:
        address_model = self._serializer.validated_data.get("address_model")
        return address_model.latitude, address_model.longitude

    def _get_estimated_distance_min(
        self, latitud_client: Decimal, longitud_client: Decimal
    ) -> list[int | Decimal]:

        list_distance: list[list[int | Decimal]] = []

        for e in self._driver_model_repository.get_all_is_available():
            latitud_driver = e.latitude
            longitude_driver = e.longitude
            distance = calculate_distance(
                (latitud_client, longitud_client), (latitud_driver, longitude_driver)
            )
            list_distance.append([e.id, distance])
        return min(list_distance, key=lambda x: x[1])

    def _get_coordinates_driver(self, driver_model_id: int) -> tuple[Decimal, Decimal]:
        driver_model = self._driver_model_repository.get_detail(driver_model_id)
        return driver_model.latitude, driver_model.longitude

    def _get_estimated_time(self, origin, destiny) -> int | None:
        url = env.get("URL_ESTIMATE_TIME")
        url = url.format(
            longitude_origin=str(origin[0]),
            latitude_origin=str(origin[1]),
            longitude_destiny=str(destiny[0]),
            latitude_destiny=str(destiny[1]),
        )

        response = requests.get(url)
        if response.status_code != 200:
            return None

        data = response.json()

        if "routes" in data:
            duracion_segundos = data["routes"][0]["duration"]
            return duracion_segundos / 60
        return None
