from django.conf.urls import patterns, url

from profiles import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	# ex: /admin/profile/5/
	url(r'^(?P<profile_id>\d+)/$', views.detail, name='detail'),
)