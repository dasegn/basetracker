from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
from django.core.urlresolvers import reverse_lazy

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:    
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/project/', include('projects.urls')),
    url(r'^admin/', include(admin.site.urls), name='admin'),
    url(r'^$', RedirectView.as_view(url='admin'), name='redirect_home'),
)
