from django.conf.urls import patterns, url

from bt.views import projects

urlpatterns = patterns('',
    url(r'^$', projects.index, name='index'),
    # ex: /project/5/
    url(r'^(?P<project_id>\d+)/$', projects.detail, {}, name='detail'),
)