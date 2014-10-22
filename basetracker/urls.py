from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
from django.core.urlresolvers import reverse_lazy

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:    

    url(r'^admin/project/', include('bt.urls.projects'), name='project'),
    url(r'^admin/profile/', include('bt.urls.profiles'), name='profile'),
    url(r'^admin/', include(admin.site.urls), name='admin'),
    #url(r'^login/$', 'social_auth.views.auth', {'backend': 'facebook'}, name='login'),
    url(r'^$', RedirectView.as_view(url='admin'), name='redirect_home'),
    url('', include('django.contrib.auth.urls', namespace='auth')),
)
