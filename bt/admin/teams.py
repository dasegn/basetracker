# -*- coding: utf-8 -*-

from django.contrib import admin

# Register your models here.
from bt.models.teams import Team
from bt.forms.teams import TeamForm

from django.conf.urls import patterns, url
from django.contrib.auth.admin import GroupAdmin
from django.contrib.auth.models import Group

class TeamInLine(admin.StackedInline):
	model = Team
	form = TeamForm
	can_delete = False
	verbose_name = 'equipo'
	verbose_name_plural = 'equipos'
	classes = ('collapse open',)
	inline_classes = ('collapse open',)

# Define a new User admin
class GroupAdmin(GroupAdmin):
    inlines = (TeamInLine, )

# Esto agrega el model al admin, pero no deseamos tener otra app más
# en el listado de administración
class TeamAdmin(admin.ModelAdmin):
	def get_urls(self):
		urls = super(TeamAdmin, self).get_urls()
		my_urls = patterns('',
			url(r'^$', self.admin_site.admin_view(self.index_view), name='index'),
		)
		return my_urls + urls

	def index_view(self, request):
		return views.admin_index_view(request)


# Re-register UserAdmin
admin.site.unregister(Group)	
admin.site.register(Group, GroupAdmin)