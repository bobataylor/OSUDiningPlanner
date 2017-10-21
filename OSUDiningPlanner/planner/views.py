# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .forms import DiningHallForm

def get_dining_halls(request):
	if request.method == 'POST':
		form = DiningHallForm(request.POST)

		if form.is_valid():
			diningHalls = form.POST.getlist('my_hall')
	return render(request, 'planner/chooseDiningHalls.html')

def index(request):
	#context = {}
	return render(request, 'planner/index.html')

