from rest_framework.views import APIView

from apps.api.serializers.address_serializers.address_create_serializer import AddressModelCreateSerializer
from apps.api.serializers.address_serializers.address_detail_serializer import AddressModelDetailSerializer
from apps.api.serializers.address_serializers.address_update_serializer import AddressModelUpdateSerializer
from apps.api.repository.address_repository.address_repository import AddressModelRepository
from apps.api.logic.address_logic.address_create_logic import AddressModelCreateLogic
from apps.api.logic.address_logic.address_detail_logic import AddressModelDetailLogic
from apps.api.logic.address_logic.address_update_logic import AddressModelUpdateLogic

class AddressApiView(APIView):

    def post(self, request) -> dict:
        serializer = AddressModelCreateSerializer(data=request.data)
        repository = AddressModelRepository()
        logic = AddressModelCreateLogic(serializer, repository)
        return logic.process()
    
    def get(self, request, *args, **kwargs) -> dict:
        pk = kwargs.get("pk")
        serializer = AddressModelDetailSerializer
        repository = AddressModelRepository()
        logic = AddressModelDetailLogic(pk, serializer, repository)
        return logic.process()

    def patch(self, request, *args, **kwargs) -> dict:
        pk = kwargs.get("pk")
        serializer = AddressModelUpdateSerializer
        repository = AddressModelRepository()
        logic = AddressModelUpdateLogic(pk, request.data, serializer, repository)
        return logic.process()