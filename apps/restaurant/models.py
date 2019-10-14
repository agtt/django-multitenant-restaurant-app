from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    opening_time = models.IntegerField()
    closing_time = models.IntegerField()
