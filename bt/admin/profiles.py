# -*- coding: utf-8 -*-

from django.contrib import admin

from django.template import RequestContext
from django.conf.urls import patterns, url
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# Register your models here.
from bt.models.profiles import Profile
from bt.views import profiles


# Define an inline admin descriptor for Profile model
# which acts a bit like a singleton
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name = 'perfil'
    verbose_name_plural = 'perfiles'

# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (ProfileInline, )


# Esto agrega el model al admin, pero no deseamos tener otra app más
# en el listado de administración
class ProfileAdmin(admin.ModelAdmin):
	def get_urls(self):
		urls = super(ProfileAdmin, self).get_urls()
		my_urls = patterns('',
			url(r'^$', self.admin_site.admin_view(self.index_view), name='index'),
			#(r'^(?P<project_id>\d+)/$', views.detail, name='detail'),
		)
		return my_urls + urls

	def index_view(self, request):
		return views.admin_index_view(request)


# Re-register UserAdmin
admin.site.unregister(User)	
admin.site.register(User, UserAdmin)