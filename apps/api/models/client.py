from django.db import models

class ClientModel(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=9)    

    def __str__(self):
        return self.name
