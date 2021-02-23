from django.db import models
from location_field.models.plain import PlainLocationField


class Place(models.Model):
    source = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    date = models.DateField()
    number = models.IntegerField()
    departure = models.TimeField()
    location = PlainLocationField(based_fields=['city'], zoom=7)
