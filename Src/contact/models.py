from django.db import models


class Visitor(models.Model):
    ip_address = models.GenericIPAddressField(default='0.0.0.0',unique=True)
    dma_code = models.CharField(max_length=255, blank=True, null=True)
    area_code = models.CharField(max_length=255, blank=True, null=True)
    metro_code = models.CharField(max_length=255, blank=True, null=True)
    postal_code = models.CharField(max_length=255, blank=True, null=True)
    country_code = models.CharField(max_length=255, blank=True, null=True)
    country_code3 = models.CharField(max_length=255, blank=True, null=True)
    country_name = models.CharField(max_length=255, blank=True, null=True)
    continent = models.CharField(max_length=255, blank=True, null=True)
    region_code = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    latitude = models.CharField(max_length=255, blank=True, null=True)
    longitude = models.CharField(max_length=255, blank=True, null=True)
    time_zone = models.CharField(max_length=255, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.ip_address)
