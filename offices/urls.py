from django.conf.urls import include, url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='offices_index' ),
	# url(r'^(?P<slug>[\w\-]+)/$', views.item, name='offices_item' ),
	url(r'^(?P<id>[\d]+)/$', views.item, name='offices_item' ),
]