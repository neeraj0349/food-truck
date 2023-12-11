from django.contrib.gis.db.models import PointField
from django.db import models


class FoodTruck(models.Model):
    location_id = models.IntegerField(primary_key=True)
    applicant = models.CharField(max_length=255)
    facility_type = models.CharField(max_length=255)
    cnn = models.IntegerField()
    location_description = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    block_lot = models.CharField(max_length=255)
    block = models.CharField(max_length=255)
    lot = models.CharField(max_length=255)
    permit = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    food_items = models.TextField()
    x = models.FloatField(null=True, blank=True)
    y = models.FloatField(null=True, blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    schedule = models.CharField(max_length=255)
    days_hours = models.CharField(max_length=255)
    noi_sent = models.CharField(max_length=255)
    approved = models.DateTimeField(null=True, blank=True)
    received = models.DateField()
    prior_permit = models.CharField(max_length=255)
    expiration_date = models.DateTimeField(null=True, blank=True)
    location = PointField(max_length=255)
    fire_prevention_districts = models.IntegerField(null=True, blank=True)
    police_districts = models.IntegerField(null=True, blank=True)
    supervisor_districts = models.IntegerField(null=True, blank=True)
    zip_codes = models.IntegerField(null=True, blank=True)
    neighborhoods_old = models.CharField(max_length=255)

    def __str__(self):
        return self.applicant
