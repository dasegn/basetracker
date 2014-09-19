# -*- coding: utf-8 -*-

from django.db import models
from bt.models.projects import Project
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from utils.adminLabels import string_with_title

# Create your models here.
class Team(models.Model):	
	group = models.OneToOneField(Group, related_name='Team', unique=True)
	description = models.TextField(verbose_name=_(u'Descripción'))
	members = models.ManyToManyField(User, verbose_name=_("Miembros"))

	class Meta:
		app_label = 'bt'
	
	def __unicode__(self):
		return self.group.name



