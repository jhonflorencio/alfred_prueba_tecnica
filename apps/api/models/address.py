from django.db import models

class AddressModel(models.Model):
    name = models.CharField(max_length=200)
    reference = models.CharField(max_length=200)
    client_model = models.ForeignKey("ClientModel", on_delete=models.CASCADE)
    latitude = models.DecimalField(max_digits=20, decimal_places=15)
    longitude = models.DecimalField(max_digits=20, decimal_places=15)

    def __str__(self):
        return self.name


