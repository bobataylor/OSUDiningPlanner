# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models



class Location(models.Model):
    location_name = models.CharField(max_length=200, primary_key=True)
    address = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.PositiveIntegerField()
    dining_style = models.CharField(max_length=200, null=True, blank=True)
    icon_URL = models.URLField(max_length=200, null=True, blank=True)
    photo_URL = models.URLField(max_length=200, null=True, blank=True)
    thumbnail_URL = models.URLField(max_length=200, null=True, blank=True)
    cuisines = models.CharField(max_length=200)
    summary = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    is_day_specific = models.BooleanField()
    location_menu = models.TextField()
    def __str__(self):
        return self.location_name

class Food(models.Model):
    class Meta:
        unique_together = (('name', 'location'),)
    name = models.CharField(max_length=200, primary_key=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    portion_size = models.CharField(max_length=200)
    course = models.CharField(max_length=200)
    ingredients = models.TextField()
    requirement = models.CharField(max_length=200)
    allergen = models.CharField(max_length=200)
    calories = models.PositiveIntegerField(default=0)
    total_fat = models.CharField(max_length=200)
    saturated_fat = models.CharField(max_length=200)
    trans_fat = models.CharField(max_length=200)
    cholestrol = models.CharField(max_length=200)
    sodium = models.CharField(max_length=200)
    total_carbohydrates = models.CharField(max_length=200)
    dietary_fiber = models.CharField(max_length=200)
    sugars = models.CharField(max_length=200)
    protein = models.CharField(max_length=200)
    vitamin_a = models.CharField(max_length=200)
    vitamin_c = models.CharField(max_length=200)
    calcium = models.CharField(max_length=200)
    iron = models.CharField(max_length=200)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
