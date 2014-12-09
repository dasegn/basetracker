# -*- coding: utf-8 -*-

from datetime import datetime
from decimal import Decimal

from django.db import models
from bt.models.projects import Project
from django.contrib.auth.models import User, Group

from django.db.models import Count, Sum
from django.utils.translation import ugettext as _
from utils.adminLabels import string_with_title
from utils.utils import get_color_overload

# Create your models here.
class Team(models.Model):	
	group = models.OneToOneField(Group, related_name='team', unique=True)
	description = models.TextField(verbose_name=_(u'Descripción'))
	members = models.ManyToManyField(User, verbose_name=_("Miembros"))

	def get_team_totals(self, year=datetime.now().isocalendar()[0], week=datetime.now().isocalendar()[1]):
		class SkelTeam: pass
		elements = []
		acum_hours = Decimal(0.0)
		for user in self.group.user_set.all():
			elem = SkelTeam()
			elem.user = user
			elem.all_hours = user.profile.get_week_hours('all',year, week)
			elem.cur_hours = user.profile.get_week_hours('Vigente',year, week)
			elem.ini_hours = user.profile.get_week_hours('Iniciativa',year, week)
			elem.pro_hours = user.profile.get_week_hours('Prospección',year, week)
			elem.overload = get_color_overload(elem.all_hours['percent'])
			acum_hours += elem.all_hours['hours']
			elements.append(elem)

		# Add Team totals
		return ({
			'elems': elements,
			'total_hours': acum_hours,
		})

	class Meta:
		app_label = 'bt'	

	def __unicode__(self):
		return self.group.name



