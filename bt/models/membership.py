# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from bt.models.attributes import Attribute
from django.utils.translation import ugettext as _
from utils.adminLabels import string_with_title
from django.contrib.admin.widgets import FilteredSelectMultiple

# Create your models here.

class Membership(models.Model):
	

	objects = models.Manager()

	def __unicode__(self):
		return self.name
	
	def save(self, *args, **kwargs):
		if not self.date_modified:
			self.date_modified = timezone.now()

		super().save(*args, **kwargs)


	class Meta:
		verbose_name = 'Proyecto'
		verbose_name_plural = 'Proyectos'
		app_label = string_with_title('bt', u'Módulos')
		ordering = ('name', 'status', 'type',)