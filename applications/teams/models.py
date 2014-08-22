# encoding: utf-8

from django.db import models
from applications.projects.models import Project
from django.utils.translation import ugettext as _


# Create your models here.
class Team(models.Model):	
	id = models.AutoField(primary_key=True, unique=True)
	name = models.CharField(verbose_name=_("Nombre"), max_length=255)
	description = models.TextField(verbose_name=_(u'Descripción'))
	projects = models.ManyToManyField(Project, verbose_name=_("Proyectos"))

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name = 'Equipo'
		verbose_name_plural = 'Equipos'	
