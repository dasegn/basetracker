# -*- coding: utf-8 -*-

from django.contrib import admin

from bt.models.tasks import Task, TaskList, Comment
from bt.forms.tasks import TaskForm, TaskListForm


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
	list_display = ('author', 'date', 'tasklist')
	list_filter = ['author','tasklist']
	ordering = ['author', 'date', 'tasklist']
	search_fields = ['body']



admin.site.register(TaskList, TaskListAdmin)
admin.site.register(Comment, CommentAdmin)
