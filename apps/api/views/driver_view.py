from rest_framework.views import APIView

from apps.api.serializers.driver_serializers.driver_create_serializer import DriverModelCreateSerializer
from apps.api.serializers.driver_serializers.driver_detail_serializer import DriverModelDetailSerializer
from apps.api.serializers.driver_serializers.driver_update_serializer import DriverModelUpdateSerializer
from apps.api.repository.driver_repository.driver_repository import DriverModelRepository
from apps.api.logic.driver_logic.driver_create_logic import DriverModelCreateLogic
from apps.api.logic.driver_logic.driver_detail_logic import DriverModelDetailLogic
from apps.api.logic.driver_logic.driver_update_logic import DriverModelUpdateLogic

class DriverApiView(APIView):

    def post(self, request) -> dict:
        serializer = DriverModelCreateSerializer(data=request.data)
        repository = DriverModelRepository()
        logic = DriverModelCreateLogic(serializer, repository)
        return logic.process()

    def get(self, request, *args, **kwargs) -> dict:
        pk = kwargs.get("pk")
        serializer = DriverModelDetailSerializer
        repository = DriverModelRepository()
        logic = DriverModelDetailLogic(pk, serializer, repository)
        return logic.process()

    def patch(self, request, *args, **kwargs) -> dict:
        pk = kwargs.get("pk")
        serializer = DriverModelUpdateSerializer
        repository = DriverModelRepository()
        logic = DriverModelUpdateLogic(pk, request.data, serializer, repository)
        return logic.process()
