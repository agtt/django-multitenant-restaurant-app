from django.db import models


class Table(models.Model):
    name = models.CharField(max_length=250, verbose_name="Table Name")
    no = models.CharField(max_length=150, verbose_name="Table No or Name")
