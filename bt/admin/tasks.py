# -*- coding: utf-8 -*-

from django.contrib import admin

from bt.models.tasks import Task, TaskList, Comment

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'list', 'priority', 'due_date')
    list_filter = ['list',]
    ordering = ['priority']
    search_fields = ['name']


admin.site.register(TaskList)
admin.site.register(Comment)
admin.site.register(Task, TaskAdmin)