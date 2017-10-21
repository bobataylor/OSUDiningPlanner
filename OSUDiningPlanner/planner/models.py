# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Food(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    portionSize = models.PositiveIntegerField()


class Location(models.Model):
