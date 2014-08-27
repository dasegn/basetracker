# -*- coding: utf-8 -*-

from django.contrib import admin

# Register your models here.
from bt.models.projects import Project
from bt.forms.projects import ProjectForm

class ProjectAdmin(admin.ModelAdmin):
	form = ProjectForm
	list_display = ('name','identifier','access','date_begin','date_end')	
	search_fields = ['name']

	def get_readonly_fields(self, request, obj = None):
		if obj: #In edit mode
			return ('identifier',) + self.readonly_fields
		return self.readonly_fields
		
admin.site.register(Project,ProjectAdmin)