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
	return render(request, 'planner/results.html')

#class ResultsView(generic.DetailView):
#	model = Food
#	template_name = 'planner/results.html'