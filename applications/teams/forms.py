#-*- coding: utf-8 -*-

from django import forms
from django.forms import ModelForm
from django.contrib.admin import widgets 
from applications.teams.models import Team
from django.utils.translation import ugettext as _

class TeamForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(TeamForm, self).__init__(*args, **kwargs)	

	class Meta:
		model = Team