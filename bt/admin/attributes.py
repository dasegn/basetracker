# -*- coding: utf-8 -*-

from django.contrib import admin

# Register your models here.
from bt.models.attributes import Attribute

class AttributeAdmin(admin.ModelAdmin):
    search_fields = ('label', 'type')
    list_display = ('label', 'type')
    list_filter = ('type')
    ordering = ('type')  # Django honors only first field.

		
admin.site.register(Attribute,AttributeAdmin)