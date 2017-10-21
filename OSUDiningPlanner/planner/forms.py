from django.forms import ModelForm
from .models import Location

class DiningHallForm(ModelForm):
	class Meta:
		model = Location
		fields = ['location_name',]