# -*- coding: utf-8 -*-

from django.db import models
from bt.views import projects
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from utils.adminLabels import string_with_title
from django.contrib.admin.widgets import FilteredSelectMultiple

# Create your models here.

class Project(models.Model):
	PUBLIC = 0
	PRIVATE = 1
	Access = (
		(PUBLIC,'Público'),
		(PRIVATE, 'Privado'),
	)
	StatusOptions = (
		(1,'Abierto'),
		(0, 'Cerrado'),
	)
	id = models.AutoField(primary_key=True, unique=True)
	name = models.CharField(verbose_name=_("Nombre"), max_length=255)
	description = models.TextField(verbose_name=_(u'Descripción'))	
	identifier = models.CharField( verbose_name=_("Identificador"), max_length=255)
	parent = models.ForeignKey('self', verbose_name=_("Proyecto padre"), default=0, null=True, blank=True)	
	access = models.IntegerField(verbose_name=_("Acceso"), default=PUBLIC,choices=Access)
	date_begin = models.DateTimeField(verbose_name=_("Fecha de inicio"), null=True)
	date_end = models.DateTimeField(verbose_name=_("Fecha de fin"), null=True)
	status = models.IntegerField(verbose_name=_("Estado"), default=1, choices=StatusOptions)
	users = models.ManyToManyField(User, verbose_name=_("Miembros"))

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name = 'Proyecto'
		verbose_name_plural = 'Proyectos'
		app_label = string_with_title('bt', u'Módulos')