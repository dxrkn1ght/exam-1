from django.db import models

class Taxi(models.Model):
    name = models.CharField(max_length=100)
    license_plate = models.CharField(max_length=20)
    driver_name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    model = models.CharField(max_length=50)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.name
