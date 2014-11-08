#-*- coding: utf-8 -*-

from django import forms
from django.forms import ModelForm
from django.contrib.admin import widgets 
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from django.contrib.admin.widgets import FilteredSelectMultiple
from bt.models.tasks import Task, TaskList, TaskListSummary
from django.conf import settings

class TaskListForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(TaskListForm, self).__init__(*args, **kwargs)	

		#list_start = forms.DateField(widget=forms.widgets.DateInput(format="%Y-%m-%d")) 

	class Media:
		css = { 'all' : ( settings.STATIC_URL + 'css/chosen.css', ) }
		js = (
			settings.STATIC_URL + 'js/jquery.min.js',
			settings.STATIC_URL + 'js/chosen.jquery.min.js',
			settings.STATIC_URL + 'js/chosen.init.js',
			settings.STATIC_URL + 'grappelli/jquery/ui/js/jquery-ui-1.10.3.custom.min.js',
			settings.STATIC_URL + 'js/jquery.weekpicker.js',
			settings.STATIC_URL + 'js/bt.tasklist.js',
		)

	class Meta:
		model = TaskList
		widgets = {
			'name' : forms.TextInput(
				attrs={ 
					'readonly': 'readonly',
					'class' : 'listName'
				}
			),
			#'project' : forms.Select(attrs={'class': 'chosen-select'}),
			#'service' : forms.Select(attrs={'class': 'chosen-select'}),
			'list_start' : forms.DateInput(
				format = '%Y-%m-%d',
				attrs= {
					'format' : '%Y-%m-%d',
					'class': 'startField weekpicker' 
				}
			),
			'list_end': forms.DateInput(
				format = '%Y-%m-%d',
				attrs = {
					'format' : '%Y-%m-%d',
					'class': 'endField',
					'readonly': 'readonly'
				}
			),
		}		

class TaskListSummaryForm(forms.ModelForm):
	class Meta:
		model = TaskListSummary
		widgets = {
			#'assigned' : forms.Select(attrs={'class': 'chosen-select'}),
		}



class TaskForm(forms.ModelForm):

	class Meta:
		model = Task
		widgets = {
			#'title': forms.TextInput(attrs={'style': "width:"}),
			'description': forms.Textarea(attrs={ 'cols': 33 , 'rows' : 6 }),
		}		