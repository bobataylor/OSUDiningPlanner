# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from django.template import loader

from .models import Food, Location

def index(request):
	return render(request, 'planner/index.html')

def results(request):
	food_list = Food.objects.filter(location="Union Market")
	return render(request, 'planner/results.html', {'food_list' : food_list})