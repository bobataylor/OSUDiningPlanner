from django import forms
from .models import Location

class DiningHallForm(forms.Form):
	diningHalls = forms.ModelMultipleChoiceField(
		queryset = ['hello', 'world'],
		widget = forms.CheckboxSelectMultiple,
	)