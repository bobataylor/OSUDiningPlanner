# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .forms import DiningHallForm
from django.views.generic.edit import CreateView
from .models import Location

def get_dining_halls(request):
	halls = {'scott', 'curl', 'marketplace', 'terrabyte cafe'}
	print halls
	if request.method == 'POST':
		form = DiningHallForm(request.POST)

		if form.is_valid():
			diningHalls = form.POST.getlist('my_hall')
	return render(request, 'planner/chooseDiningHalls.html', {"hallList" : halls})


def index(request):
	#context = {}
	return render(request, 'planner/index.html')

