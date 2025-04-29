from django.urls import path

from apps.api.views.driver_view import DriverApiView
from apps.api.views.address_view import AddressApiView
from apps.api.views.service_view import ServiceApiView

urlpatterns = [
    
    path(r'driver', DriverApiView.as_view(), name='driver'),
    path(r'driver/<int:pk>', DriverApiView.as_view(), name='driver-detail'),
    path(r'address', AddressApiView.as_view(), name='address'),
    path(r'address/<int:pk>', AddressApiView.as_view(), name='address-detail'),
    path(r'service', ServiceApiView.as_view(), name='service'),
]