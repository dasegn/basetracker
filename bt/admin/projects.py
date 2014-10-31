# -*- coding: utf-8 -*-

from django.contrib import admin
from django.conf import settings

# Register your models here.
from bt.models.projects import Project, Comment
from bt.models.membership import Membership

from bt.forms.projects import ProjectForm, CommentForm
from bt.forms.membership import MembershipForm
from bt.admin.roles import RoleInline
from utils.readonlywidget import ReadOnlyWidget

class MembershipAdmin(admin.ModelAdmin):
	list_display = ['project', 'role', 'user']
	list_display_links = list_display
	list_filter = ['project__name', 'user__username']
	form = MembershipForm


class MembershipInline(admin.TabularInline):
	model = Membership
	extra = 0
		

class ProjectAdmin(admin.ModelAdmin):
	add_form_template = settings.BASE_DIR + '/templates/admin/projects/change_form.html'
	change_form_template = settings.BASE_DIR + '/templates/admin/projects/change_form.html'
	form = ProjectForm
	list_display = ('name','identifier','access','type','status')
	search_fields = ['name','identifier']
	list_filter = ['access','type','status','client']

	fieldsets = (
		('General', {
			'classes' : ('general',),
			'fields': ('name', 'description', 'identifier', 'parent', 'access')
		}),
		('Atributos', {
			'classes' : ('atributos',),
			'fields': ('type', 'status', 'kam', 'admin', 'rd', 'client')
		}),	
		('Servicios', {
			'classes' : ('servicios',),
			'fields': ('services',)
		}),			
		('Fechas', {
			'classes' : ('fechas',),
			'fields': ('date_begin', 'date_end', 'date_created', 'date_modified')
		}),			
	)

	inlines = [RoleInline, MembershipInline,]

	def add_view(self, request, form_url='', extra_context=None):
		extra_context = extra_context or {}
		#extra_context['tabs'] = self.tabs
		return super(ProjectAdmin, self).add_view(request,
			form_url, extra_context=extra_context)

	def get_readonly_fields(self, request, obj = None):
		if obj: #In edit mode
			return ('identifier','date_created','date_modified',) + self.readonly_fields
		return ('date_created','date_modified',) + self.readonly_fields

class CommentAdmin(admin.ModelAdmin):
	list_display = ('author', 'project', 'submit_date')
	list_filter = ['author','project__name']
	ordering = ['author', 'project', 'submit_date']
	search_fields = ['author__username', 'project__name', 'body']

	form = CommentForm
	readonly_fields = ['submit_date']
	
	def formfield_for_foreignkey(self, db_field, request, **kwargs):
		if (db_field.name in ["author",]):
			kwargs['initial'] = request.user.id
			return db_field.formfield(**kwargs)
		return super(CommentAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

	def formfield_for_dbfield(self, db_field, **kwargs):
		if (db_field.name in ["author",]):
			kwargs["widget"] = ReadOnlyWidget(db_field=db_field)
		return super(CommentAdmin, self).formfield_for_dbfield(db_field, **kwargs)

		
admin.site.register(Project,ProjectAdmin)
admin.site.register(Membership, MembershipAdmin)
admin.site.register(Comment, CommentAdmin)
