# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Food(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    portionSize = models.PositiveIntegerField()


class Location(models.Model):
    location_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.PositiveIntegerField()
    dining_style = models.CharField(max_length=200)
    icon_URL = models.URLField(max_length=200)
    photo_URL = models.URLField(max_length=200)
    thumbnail_URL = models.URLField(max_length=200)
    cuisines = models.CharField(max_length=200)
    summary = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    is_day_specific = models.BooleanField()
    location_menu = models.TextField()
