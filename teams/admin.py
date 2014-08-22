from django.contrib import admin

# Register your models here.
from teams.models import Team
from teams.forms import TeamForm

class TeamAdmin(admin.ModelAdmin):
	form = TeamForm

admin.site.register(Team,TeamAdmin)
