from django.contrib import admin

# Register your models here.
from applications.teams.models import Team
from applications.teams.forms import TeamForm

class TeamAdmin(admin.ModelAdmin):
	form = TeamForm

admin.site.register(Team,TeamAdmin)
