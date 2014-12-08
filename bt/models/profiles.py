# -*- coding: utf-8 -*-

from datetime import datetime

from django.db import models
from django.contrib.auth.models import User
from django.db.models import Count, Sum
from django.db.models.signals import post_save
from django.utils.translation import ugettext as _
from utils.adminLabels import string_with_title
from django.conf import settings

from bt.models.projects import Project
from bt.models.tasks import Task, TaskList, TaskListSummary

# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(User, related_name='profile', unique=True)
	hours_per_week = models.DecimalField(
		verbose_name=_("Horas por semana"), 
		max_digits=8, 
		decimal_places=2, 
		default=30,
		null=True
	)
	skype = models.CharField(verbose_name=_("Skype"), max_length=100, default='', null=True, blank=True)
	avatar = models.ImageField(verbose_name=_("Avatar"), upload_to='.', default='', null=True, blank=True)
	
	class Meta:
		app_label = string_with_title('bt', u'Módulos')

	def __unicode__(self):
		return self.user.username



	def get_avatar_url(self):
		if self.avatar == '':
			return '%sdefault.jpg' % (
				settings.MEDIA_URL,
			)			
		else:		
			return '%s%s' % (
				settings.MEDIA_URL,
				self.avatar,
			)

	def get_week_hours(self, lstype='all', year=datetime.now().isocalendar()[0], week=datetime.now().isocalendar()[1]):
		if (lstype == 'Vigente') or (lstype == 'Iniciativa') or (lstype == 'Prospección'):
			memb = User.objects.get(id=self.user.id).memberships.filter(project__type__label=lstype).values_list('id', flat=True)
		else:
			memb = User.objects.get(id=self.user.id).memberships.values_list('id', flat=True)
		qs = TaskList.objects.filter(name=('Semana %d %d' % (week, year))).filter(tasklistsummary__assigned__in=memb).aggregate(sum_hours=Sum('tasklistsummary__hours'))
		values = {}
		values['hours'] = qs['sum_hours']
		try:
			values['percent'] = (qs['sum_hours'] / self.hours_per_week) * 100
		except (ValueError, TypeError, ZeroDivisionError):
			values['percent'] = 0
		return values


def create_user_profile(sender, instance, created, **kwargs):
	"""Create the UserProfile when a new User is saved"""
	if created:
		Profile.objects.create(user=instance)
	else:
		try:
			Profile.objects.get(user=instance)
		except Profile.DoesNotExist:
			Profile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)