from django.conf.urls import include, url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='clients_index' ),
	# url(r'^(?P<slug>[\w\-]+)/$', views.item, name='clients_item' ),
	url(r'^(?P<id>[\d]+)/$', views.item, name='clients_item' ),
]