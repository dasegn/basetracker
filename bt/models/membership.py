# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from bt.models.attributes import Attribute
from bt.models.projects import Project

from django.utils.translation import ugettext as _
from utils.adminLabels import string_with_title
from utils.slug import slugify_uniquely
from utils.utils import truncate_text
from django.contrib.admin.widgets import FilteredSelectMultiple

from django.core.exceptions import ValidationError
from django.core.exceptions import ObjectDoesNotExist


# Create your models here.

class Role(models.Model):
	name = models.CharField(max_length=200, null=False, blank=False, verbose_name=_("Nombre"))
	slug = models.SlugField(max_length=250, null=True, blank=True, verbose_name=_("slug"))
	project = models.ForeignKey(Project, null=True, blank=False, related_name="roles", verbose_name=_("Proyecto"))

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify_uniquely(self.name, self.__class__)

		super(Role, self).save(*args, **kwargs)
	
	def __str__(self):
		return self.name

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name = "rol"
		verbose_name_plural = "roles"
		ordering = ["name", "slug"]
		app_label = string_with_title('bt', u'Módulos')
		unique_together = (("slug", "project"),)
		#permissions = (
		#	("view_role", "Can view role"),
		#)



class Membership(models.Model):
	user = models.ForeignKey(User, null=True, blank=False, default=None, related_name="memberships", verbose_name=_("Usuario"))
	project = models.ForeignKey('Project', null=False, blank=False, related_name="memberships", verbose_name=_("Proyecto"))
	role = models.ForeignKey('Role', null=False, blank=False, related_name="memberships", verbose_name=_("Rol"))

	def __str__(self):
		return u'%s - %s - %s' % (
			truncate_text(self.project.name, 80),
			self.user.get_full_name(),			
			self.role.name
		)	

	def __unicode__(self):
		return u'%s - %s - %s' % (
			truncate_text(self.project.name, 80),
			self.user.get_full_name(),			
			self.role.name
		)		
	def get_user_full(self):
		return u'%s' % (self.user.get_full_name())	

	get_user_full.short_description = 'Usuario'

	def clean(self):
		# TODO: Review and do it more robust
		try: 
			memberships = Membership.objects.filter(user=self.user, project=self.project, role=self.role)
			if self.pk == None and memberships.count() > 0:
				raise ValidationError(_('El usuario %s ya es miembro de este proyecto con el rol %s' % (self.user, self.role.name) ))
		except ObjectDoesNotExist:
			raise ValidationError(_('Por favor, introduzca todos los campos requeridos'))


	class Meta:
		verbose_name = u'membresia'
		verbose_name_plural = u'membresias'
		#unique_together = ("user", "rol",)
		app_label = string_with_title('bt', u'Módulos')
		ordering = ('project', 'user',)