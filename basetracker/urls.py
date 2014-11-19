from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
from django.core.urlresolvers import reverse_lazy
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from bt.viewsets.projects import ProjectViewSet, CommentViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()

router.register(r'projects', ProjectViewSet)
router.register(r'comments', CommentViewSet)


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:    
    (r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^api/v1/', include(router.urls)),
    url(r'^api/v1/api-auth/', include('rest_framework.urls', namespace='rest_framework')),    
    url(r'^chaining/', include('smart_selects.urls')),
    url(r'^admin/project/', include('bt.urls.projects'), name='project'),
    url(r'^admin/profile/', include('bt.urls.profiles'), name='profile'),
    url(r'^admin/', include(admin.site.urls), name='admin'),
    url('', include('django.contrib.auth.urls', namespace='auth'))

)


