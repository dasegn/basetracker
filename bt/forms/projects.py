#-*- coding: utf-8 -*-

from django import forms
from django.forms import ModelForm
from django.contrib.admin import widgets 
from bt.models.projects import Project
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from django.utils.translation import ugettext as _
from django.contrib.admin.widgets import FilteredSelectMultiple

# Importación de app de utilerías 
from utils.forms import NestedModelChoiceField

class ProjectForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(ProjectForm, self).__init__(*args, **kwargs)
		self.fields['date_begin'].required = False
		self.fields['date_end'].required = False
		self.fields['description'].required = False

		self.fields['users'].required = False
		self.fields['groups'].required = False

		self.fields['type'].required = False
		self.fields['status'].required = False
		self.fields['kam'].required = False
		self.fields['admin'].required = False
		self.fields['rd'].required = False
		self.fields['client'].required = False

	parent = NestedModelChoiceField(queryset=Project.objects.all(),
									related_name= 'project_set',
									parent_field= 'parent_id',
									label_field= 'name',
									required = False,
									label= _('Proyecto padre'),
									empty_label= _('Elige un proyecto'))

	users = forms.ModelMultipleChoiceField(
		queryset=User.objects.all(),
		required=False,
		widget=FilteredSelectMultiple(
			verbose_name='Miembros',
			is_stacked=False
		)
	)

	groups = forms.ModelMultipleChoiceField(
		queryset=Group.objects.all(),
		required=False,
		widget=FilteredSelectMultiple(
			verbose_name='Grupos',
			is_stacked=False
		)
	)

	class Meta:
		model = Project