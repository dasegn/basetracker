# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from bt.models.projects import Project
from bt.models.attributes import Attribute
from utils.adminLabels import string_with_title


class Service(models.Model):
	id = models.AutoField(primary_key=True, unique=True)
	name = models.CharField(verbose_name=_("Nombre del servicio"), max_length=255)
	description = models.TextField(verbose_name=_(u'Descripción'))	

	objects = models.Manager()

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name = 'Servicio'
		verbose_name_plural = 'Servicios'
		app_label = string_with_title('bt', u'Módulos')
