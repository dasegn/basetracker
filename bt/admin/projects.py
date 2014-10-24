# -*- coding: utf-8 -*-

from django.contrib import admin

# Register your models here.
from bt.models.projects import Project
from bt.forms.projects import ProjectForm


class ProjectAdmin(admin.ModelAdmin):
	form = ProjectForm
	list_display = ('name','identifier','access','type','status')
	search_fields = ['name','identifier']
	list_filter = ['access','type','status','client']

	fieldsets = (
		(None, {
			'fields': ('name', 'description', 'identifier', 'parent', 'access')
		}),
		('Atributos', {
			'classes': ('collapse','extrapretty'),
			'fields': ('type', 'status', 'kam', 'admin', 'rd', 'client')
		}),
		('Miembros', {
			'classes': ('collapse',),
			'fields': ('users', 'groups')
		}),	
		('Servicios', {
			'classes': ('collapse',),
			'fields': ('services',)
		}),			
		('Fechas', {
			'classes': ('collapse',),
			'fields': ('date_begin', 'date_end', 'date_created', 'date_modified')
		}),	
	)


	def get_readonly_fields(self, request, obj = None):
		if obj: #In edit mode
			return ('identifier','date_created','date_modified',) + self.readonly_fields
		return self.readonly_fields
		
admin.site.register(Project,ProjectAdmin)