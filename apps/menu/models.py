from django.db import models
from apps.restaurant.models import Restaurant


class Menu(models.Model):
    name = models.CharField(max_length=512, null=True, blank=True, verbose_name="Menu Name")
    restaurant = models.ForeignKey(Restaurant, null=True, blank=True, on_delete=models.CASCADE,
                                   related_name="menu_restaurant",
                                   verbose_name="Restaurant")
