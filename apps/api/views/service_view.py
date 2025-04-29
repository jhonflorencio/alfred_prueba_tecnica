from rest_framework.views import APIView

from apps.api.serializers.service_serializers.service_create_serializer import ServiceModelCreateSerializer
from apps.api.repository.service_repository.service_repository import ServiceModelRepository
from apps.api.logic.service_logic.service_create_logic import ServiceModelCreateLogic

class ServiceApiView(APIView):

    def post(self, request) -> dict:
        serializer = ServiceModelCreateSerializer(data=request.data)
        repository = ServiceModelRepository()
        logic = ServiceModelCreateLogic(serializer, repository)
        return logic.process()
