from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^get_dining_halls$', views.get_dining_halls, name='get_dining_halls')
]
