from django.conf.urls import patterns, url

from bt.views import profiles

urlpatterns = patterns('',
	url(r'^$', profiles.index, name='index'),
	# ex: /admin/profile/5/
	url(r'^(?P<profile_id>\d+)/$', profiles.detail, name='detail'),
)