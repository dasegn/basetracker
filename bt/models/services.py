# -*- coding: utf-8 -*-

from django.db import models

from utils.adminLabels import string_with_title
from django.utils.translation import ugettext as _

class Service(models.Model):
	id = models.AutoField(primary_key=True, unique=True)
	name = models.CharField(verbose_name=_("Nombre del servicio"), null=False, blank=False, max_length=255)
	description = models.TextField(verbose_name=_(u'Descripción'))	

	objects = models.Manager()

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name = 'servicio'
		verbose_name_plural = 'servicios'
		app_label = string_with_title('bt', u'Módulos')
