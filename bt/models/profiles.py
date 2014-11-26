# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils.translation import ugettext as _
from utils.adminLabels import string_with_title
from django.db.models.signals import post_save
from django.conf import settings

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