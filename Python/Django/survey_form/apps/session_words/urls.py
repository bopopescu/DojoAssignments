from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^$', views.index),
	url(r'^result$', views.create),
	url(r'^create$', views.create),
	url(r'^clear$', views.clear)
]