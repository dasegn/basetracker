#-*- coding: utf-8 -*-

from django import forms
from django.forms import ModelForm
from django.contrib.admin import widgets 
from bt.models.teams import Team
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from django.contrib.admin.widgets import FilteredSelectMultiple

class TeamForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(TeamForm, self).__init__(*args, **kwargs)	

	class Meta:
		model = Team