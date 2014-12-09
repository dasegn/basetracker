# -*- coding: utf-8 -*-

from django.contrib import admin
from bt.models.tasks import Task, TaskList, TaskListSummary
from bt.forms.tasks import TaskForm, TaskListForm, TaskListSummaryForm

from django.forms.models import BaseInlineFormSet

class TaskInline(admin.TabularInline):
	model = Task
	extra = 0
	form = TaskForm

	exclude = ('completed_date','created_date', 'created_by')

	def formfield_for_foreignkey(self, db_field, request, **kwargs):
		if (db_field.name in ["created_by",]):
			kwargs['initial'] = request.user.id
			return db_field.formfield(**kwargs)
		return super(TaskInline, self).formfield_for_foreignkey(db_field, request, **kwargs)


class TaskListSummaryInlineFormset(BaseInlineFormSet):
	def __init__(self, *args, **kwargs):
		super(TaskListSummaryInlineFormset, self).__init__(*args, **kwargs)

		
	def add_fields(self, form, index):
		super(TaskListSummaryInlineFormset, self).add_fields(form, index)



class TaskListSummaryInline(admin.TabularInline):
	model = TaskListSummary
	extra = 0
	form = TaskListSummaryForm
	formset = TaskListSummaryInlineFormset

class TaskListAdmin(admin.ModelAdmin):
	list_display = ('name', 'project', 'service', 'week_number','count_tasks','progress_tasks',)
	list_filter = ['name', 'project__name', 'service']

	ordering = ['name', 'project']
	search_fields = ['name', 'project__name']

	inlines = [TaskInline, TaskListSummaryInline, ]

	form = TaskListForm

	fieldsets = (
		('Detalles de la lista', {
			'classes' : ('general',),
			'fields': ('name', ('project', 'service'), ('list_start', 'list_end'))
		}),		
	)

	def save_formset(self, request, form, formset, change):
		instances = formset.save(commit=False)
		for instance in instances:
			if isinstance(instance, Task):
				if(not instance.created_by):
					instance.created_by = request.user
			instance.save()


class TaskAdmin(admin.ModelAdmin):
	list_display = ('title', 'list', 'priority', 'due_date')
	search_fields = ['name']





admin.site.register(TaskList, TaskListAdmin)
