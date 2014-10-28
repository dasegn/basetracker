#-*- coding: utf-8 -*-

from django import forms
from django.forms import ModelForm
from django.contrib.admin import widgets 
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from django.contrib.admin.widgets import FilteredSelectMultiple
from bt.models.tasks import Task, TaskList, Comment

class TaskListForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(TaskListForm, self).__init__(*args, **kwargs)	



	class Media:
		js = (
			'/static/admin/pageadmin.js',
		)

	class Meta:
		model = TaskList

class CommentForm(forms.ModelForm):

	class Meta:
		model = Comment

class TaskForm(forms.ModelForm):



	class Meta:
		model = Task
		widgets = {
			'description': forms.Textarea(attrs={'cols': 20}),
			'hours': forms.NumberInput(attrs={'style': 'width: 70px'})
		}		