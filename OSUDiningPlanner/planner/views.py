# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from django.template import loader
from .forms import DiningHallForm
from django.views.generic.edit import CreateView
from .models import Location

from .models import Food, Location

def get_dining_halls(request):
	halls = Location.objects.all()
	print halls
	if request.method == 'POST':
		form = DiningHallForm(request.POST)

		if form.is_valid():
			diningHalls = form.POST.getlist('my_hall')
			print(diningHalls)
			diningHalls = form.save()
	return render(request, 'planner/chooseDiningHalls.html', {"hallList" : halls})



def index(request):
	return render(request, 'planner/index.html')


def results(request):
	food_list = Food.objects.filter(location="Union Market")
	return render(request, 'planner/results.html', {'food_list' : food_list})

