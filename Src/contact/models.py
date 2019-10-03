from django.db import models


class Visitor(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    ip_address = models.GenericIPAddressField(default='0.0.0.0',unique=True)
    latitude = models.CharField(max_length=255, blank=True, null=True)
    longitude = models.CharField(max_length=255, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.ip_address)
