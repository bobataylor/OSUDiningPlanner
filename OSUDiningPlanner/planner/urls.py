from django.conf.urls import url

from . import views

app_name = 'planner'

urlpatterns = [
	url(r'^$', views.index, name="index"),
	url(r'^results$', views.results, name='result'),
	url(r'^get_dining_halls$', views.get_dining_halls, name='get_dining_halls'),
]
