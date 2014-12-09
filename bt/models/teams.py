# -*- coding: utf-8 -*-

from datetime import datetime
from decimal import Decimal

from django.db import models
from bt.models.projects import Project
from django.contrib.auth.models import User, Group

from django.db.models import Count, Sum
from django.utils.translation import ugettext as _
from utils.adminLabels import string_with_title
from utils.utils import get_color_overload, convert_to_decimal

# Create your models here.
class Team(models.Model):	
	group = models.OneToOneField(Group, related_name='team', unique=True)
	description = models.TextField(verbose_name=_(u'Descripción'))
	members = models.ManyToManyField(User, verbose_name=_("Miembros"))

	def get_team_totals(self, year=datetime.now().isocalendar()[0], week=datetime.now().isocalendar()[1]):
		class SkelTeam: pass
		elements = []
		acum_hours = Decimal(0.0)
		count = self.group.user_set.all().count()
		for user in self.group.user_set.all():
			elem = SkelTeam()
			elem.user = user
			elem.all_hours = user.profile.get_week_hours('all',year, week)
			elem.cur_hours = user.profile.get_week_hours('Vigente',year, week)
			elem.ini_hours = user.profile.get_week_hours('Iniciativa',year, week)
			elem.pro_hours = user.profile.get_week_hours('Prospección',year, week)
			elem.overload = get_color_overload(elem.all_hours['percent'])
			acum_hours += convert_to_decimal(elem.all_hours['hours'])
			elements.append(elem)

		# Get all totals 
		avg = self.get_avg_totals(acum_hours, count)
		prom = self.get_prom_totals(avg)
		prom_sem = self.get_prom_sem(avg)

		# Add Team totals
		return ({
			'elems': elements,
			'total_hours': acum_hours,
			'total_avg': avg,
			'total_prom': prom,
			'total_sem': prom_sem
		})

	def get_avg_totals(self, totals, count):
		if count > 0:
			try:
				return (totals / Decimal(count))
			except (ZeroDivisionError, ValueError, TypeError):
				return Decimal(0.0)
		else:
			return Decimal(0.0)	

	def get_prom_totals(self, avg_total):
		if avg_total > 0:
			try:
				return ( avg_total / 5 )
			except (ZeroDivisionError, ValueError, TypeError):
				return Decimal(0.0)
		else:
			return Decimal(0.0)	

	def get_prom_sem(self, avg_total):
		if avg_total > 0:
			try:
				return ((avg_total/30) * 100)
			except (ZeroDivisionError, ValueError, TypeError):
				return Decimal(0.0)
		else:
			return Decimal(0.0)	



	class Meta:
		app_label = 'bt'	

	def __unicode__(self):
		return self.group.name



