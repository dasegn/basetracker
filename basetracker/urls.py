from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
from django.core.urlresolvers import reverse_lazy
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
admin.autodiscover()

from bt.routers import router

urlpatterns = patterns('',
    # Examples: 
    url(r'^$', 'bt.views.main.index'),

    # Login / logout.   
    url(r'^login/$', 'bt.views.auth.login_user'),
    url(r'^logout/$', 'bt.views.auth.logout_user'),

    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^api/v1/', include(router.urls)),
    url(r'^api/v1/api-auth/', include('rest_framework.urls', namespace='rest_framework')),    
    url(r'^chaining/', include('smart_selects.urls')),
    url(r'^admin/project/', include('bt.urls.projects'), name='project'),
    url(r'^admin/profile/', include('bt.urls.profiles'), name='profile'),
    url(r'^admin/', include(admin.site.urls), name='admin')   
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


