#-*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from django.contrib.admin import widgets 
from projects.models import Project
from django.utils.translation import ugettext as _

from utils.forms import NestedModelChoiceField

class ProjectForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(ProjectForm, self).__init__(*args, **kwargs)
		self.fields['date_begin'].required = False
		self.fields['date_end'].required = False
		self.fields['description'].required = False

	parent = NestedModelChoiceField(queryset=Project.objects.all(),
									related_name= 'project_set',
									parent_field= 'parent_id',
									label_field= 'name',
									required = False,
									label= _('Proyecto padre'),
									empty_label= _('Elige un proyecto'))

	class Meta:
		model = Project