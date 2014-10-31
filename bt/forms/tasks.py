#-*- coding: utf-8 -*-

from django import forms
from django.forms import ModelForm
from django.contrib.admin import widgets 
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from django.contrib.admin.widgets import FilteredSelectMultiple
from bt.models.tasks import Task, TaskList, TaskListSummary

class TaskListForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(TaskListForm, self).__init__(*args, **kwargs)	



	class Media:
		css = { 'all' : ('css/chosen.css',) }
		js = (
			'js/jquery.min.js',
			'js/chosen.jquery.min.js',
			'js/chosen.init.js',
		)

	class Meta:
		model = TaskList

class TaskListSummaryForm(forms.ModelForm):
	class Meta:
		model = TaskListSummary
		widgets = {
			'assigned' : forms.Select(attrs={'class': 'chosen-select'}),
		}



class TaskForm(forms.ModelForm):

	class Meta:
		model = Task
		widgets = {
			#'title': forms.TextInput(attrs={'style': "width:"}),
			'description': forms.Textarea(attrs={ 'cols': 33 , 'rows' : 6 }),
		}		