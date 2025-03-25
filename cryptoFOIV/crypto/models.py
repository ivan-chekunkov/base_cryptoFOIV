from django.db import models


class Packet(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    creation_date = models.DateTimeField(
        auto_now_add=True, blank=True, null=True
    )
    last_modified = models.DateTimeField(auto_now=True, blank=True, null=True)
