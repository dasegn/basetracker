# -*- coding: utf-8 -*-

from django.contrib import admin
from bt.models.tasks import Task, TaskList, Comment
from bt.forms.tasks import TaskForm, TaskListForm, CommentForm
from utils.readonlywidget import ReadOnlyWidget



class TaskInline(admin.TabularInline):
	model = Task
	extra = 0
	form = TaskForm
	
	def get_readonly_fields(self, request, obj = None):
		return ('completed_date',) + self.readonly_fields


class TaskListAdmin(admin.ModelAdmin):
	list_display = ('name', 'project')
	list_filter = ['project','name']

	ordering = ['name', 'project']
	search_fields = ['name']

	inlines = [TaskInline,]
	form = TaskListForm



class TaskAdmin(admin.ModelAdmin):
	list_display = ('title', 'list', 'priority', 'due_date')
	search_fields = ['name']


class CommentAdmin(admin.ModelAdmin):
	list_display = ('author', 'submit_date', 'tasklist')
	list_filter = ['author','tasklist']
	ordering = ['author', 'submit_date', 'tasklist']
	search_fields = ['body']

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


admin.site.register(TaskList, TaskListAdmin)
admin.site.register(Comment, CommentAdmin)
