# -*- coding: utf-8 -*-

from django.db import models
from bt.views import projects
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from bt.models.attributes import Attribute
from django.utils.translation import ugettext as _
from utils.adminLabels import string_with_title
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.utils import timezone

# Create your models here.

class Project(models.Model):

	id = models.AutoField(primary_key=True, unique=True)
	name = models.CharField(verbose_name=_("Nombre"), null=False, blank=False, max_length=255)
	description = models.TextField(null=False, blank=False, default="", verbose_name=_(u'Descripción'))
	identifier = models.CharField( verbose_name=_("Identificador"), max_length=255)
	parent = models.ForeignKey('self', verbose_name=_(u"Proyecto padre"), default=0, null=True, blank=True)
	access = models.BooleanField(default=False, null=False, blank=True, verbose_name=_("Es privado"))

	# Dates 
	date_begin = models.DateTimeField(verbose_name=_("Fecha de inicio"), null=True)
	date_end = models.DateTimeField(verbose_name=_("Fecha de fin"), null=True)
	date_created = models.DateTimeField(null=False, blank=False, verbose_name=_(u'Fecha de creación'), default=timezone.now)
	date_modified = models.DateTimeField(null=False, blank=False, verbose_name=_(u'Fecha de modificación'), default=timezone.now)
	
	# Memberships
	users = models.ManyToManyField(User,  related_name="projects", verbose_name=_("Miembros"))
	groups = models.ManyToManyField(Group, verbose_name=_("Grupos"))

	#Attributes
	type = models.ForeignKey(Attribute,  null=True, limit_choices_to={'type': 'project-type'}, related_name='projects_with_type')
	status = models.ForeignKey(Attribute,  null=True, limit_choices_to={'type': 'project-status'}, related_name='projects_with_status')
	kam = models.ForeignKey(Attribute,  null=True, limit_choices_to={'type': 'project-kam'}, related_name='projects_with_kam')
	admin = models.ForeignKey(Attribute,  null=True, limit_choices_to={'type': 'project-admin'}, related_name='projects_with_admin')
	rd = models.ForeignKey(Attribute, null=True,  limit_choices_to={'type': 'project-rd'}, related_name='projects_with_rd')
	client = models.ForeignKey(Attribute,  null=True, limit_choices_to={'type': 'project-client'}, related_name='projects_with_client')

	objects = models.Manager()

	def __unicode__(self):
		return self.name
	
	def save(self, *args, **kwargs):
		if not self.date_modified:
			self.date_modified = timezone.now()
		super(Project, self).save(*args, **kwargs)


	class Meta:
		verbose_name = 'Proyecto'
		verbose_name_plural = 'Proyectos'
		app_label = string_with_title('bt', u'Módulos')
		ordering = ('name', 'status', 'type',)