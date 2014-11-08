# -*- coding: utf-8 -*-

from django.contrib import admin

# Register your models here.
from bt.models.membership import Role



class RoleAdmin(admin.ModelAdmin):
	list_display = ["name"]


class RoleInline(admin.TabularInline):

	exclude = ('slug',)
	model = Role
	extra = 0