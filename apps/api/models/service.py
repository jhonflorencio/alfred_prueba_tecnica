from django.db import models

from apps.api.enums import ServiceStatus


class ServiceModel(models.Model):            
    address_model = models.ForeignKey("AddressModel", on_delete=models.CASCADE)
    driver_model = models.ForeignKey("DriverModel", on_delete=models.CASCADE, null=True, blank=True)
    estimated_time = models.DecimalField(decimal_places=2, max_digits=5, default=0)
    estimated_distance = models.DecimalField(decimal_places=15, max_digits=20, default=0)
    delivery_status = models.CharField(
        max_length=50,
        choices=ServiceStatus.choices(),
        default=ServiceStatus.PENDING.value        
    )

    def __str__(self):
        return self.driver_model.name

