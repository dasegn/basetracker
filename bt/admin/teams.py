# -*- coding: utf-8 -*-

from django.contrib import admin

# Register your models here.
from bt.models.teams import Team
from bt.forms.teams import TeamForm

class TeamAdmin(admin.ModelAdmin):
	form = TeamForm


admin.site.register(Team,TeamAdmin)