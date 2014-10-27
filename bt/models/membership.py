# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from bt.models.attributes import Attribute
from bt.models.projects import Project
from django.utils.translation import ugettext as _
from utils.adminLabels import string_with_title
from utils.slug import slugify_uniquely
from django.core.exceptions import ValidationError

from django.contrib.admin.widgets import FilteredSelectMultiple

# Create your models here.

class Role(models.Model):
	name = models.CharField(max_length=200, null=False, blank=False, verbose_name=_("name"))
	slug = models.SlugField(max_length=250, null=False, blank=True, verbose_name=_("slug"))
	project = models.ForeignKey(Project, null=True, blank=False, related_name="roles", verbose_name=_("project"))

	def save(self, *args, **kwargs):
	    if not self.slug:
	        self.slug = slugify_uniquely(self.name, self.__class__)

	    super(Role, self).save(*args, **kwargs)

	class Meta:
		verbose_name = "rol"
		verbose_name_plural = "roles"
		ordering = ["name", "slug"]
		app_label = string_with_title('bt', u'Módulos')
		unique_together = (("slug", "project"),)
		#permissions = (
		#	("view_role", "Can view role"),
		#)

	def __str__(self):
	    return self.name


class Membership(models.Model):
	user = models.ForeignKey(User, null=True, blank=True, default=None, related_name="memberships")
	project = models.ForeignKey('Project', null=False, blank=False, related_name="memberships")
	role = models.ForeignKey('Role', null=False, blank=False, related_name="memberships")

	def __unicode__(self):
		return self.user
	
	def clean(self):
		# TODO: Review and do it more robust
		memberships = Membership.objects.filter(user=self.user, project=self.project)
		if self.user and memberships.count() > 0 and memberships[0].id != self.id:
			raise ValidationError(_('El usuario ya es miembro de este proyecto'))


	class Meta:
		verbose_name = u'membresia'
		verbose_name_plural = u'membresias'
		unique_together = ("user", "project",)
		app_label = string_with_title('bt', u'Módulos')
		ordering = ('project', 'user',)