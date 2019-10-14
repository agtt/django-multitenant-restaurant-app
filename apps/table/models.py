from django.db import models
from apps.restaurant.models import Restaurant


class Table(models.Model):
    name = models.CharField(max_length=250, verbose_name="Table Name")
    no = models.CharField(max_length=150, verbose_name="Table No or Name")
    size = models.IntegerField()
    restaurant = models.ForeignKey(Restaurant, null=True, blank=True, on_delete=models.CASCADE,
                                   related_name="table_restaurant",
                                   verbose_name="Restaurant")
