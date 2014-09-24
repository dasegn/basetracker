# -*- coding: utf-8 -*-

from django.contrib import admin

# Register your models here.
from bt.models.services import Service

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ['name', 'description']
    ordering = ['name']  # Django honors only first field.

		
admin.site.register(Service, ServiceAdmin)