# -*- coding: utf-8 -*-

from datetime import datetime

from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from bt.models.services import Service
from bt.models.attributes import Attribute
from bt.models.tasks import TaskList

from django.contrib.auth import get_user_model
from django.utils.translation import ugettext as _
from utils.adminLabels import string_with_title
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.utils import timezone

# Aggregates imports
from django.db.models import Count, Sum
from django.db.models import Q
from utils.aggregators import Percent,PercentAggregate, CompleteCount, CompleteCountAggregate

# Create your models here.
class TotalQuerySet(models.query.QuerySet):
	def getweek(self, week, year):
		week_end = '{0} {1}'.format(week, year)
		qs = self.filter(tsklst__name__endswith=week_end)
		qs = qs.annotate(total=CompleteCount('tsklst__tsk_item'), percent=Percent('tsklst__tsk_item'))
		qs = qs.order_by('percent')
		return qs

	def danger(self):
		return self.filter(percent__gte=0, percent__lte=50)
	def warning(self):
		return self.filter(percent__gte=51, percent__lte=75)
	def success(self):
		return self.filter(percent__gte=76, percent__lte=100)

class TotalManager(models.Manager):
	"""Object manager for totals """
	def get_query_set(self):
		qs = TotalQuerySet(self.model, using=self._db)
		return qs.exclude(status__label='Cerrado')

	def getweek(self, week=datetime.now().isocalendar()[1], year=datetime.now().isocalendar()[0]):
		return self.get_query_set().getweek(week, year)

	def danger(self):
		return self.get_query_set().danger()
	def warning(self):
		return self.get_query_set().warning()
	def success(self):
		return self.get_query_set().success()


class Project(models.Model):

	id = models.AutoField(primary_key=True, unique=True)
	name = models.CharField(verbose_name=_("Nombre de proyecto"), null=False, blank=False, max_length=255)
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
	members = models.ManyToManyField(User, related_name="projects",
									through="Membership", verbose_name=_("members"))

	#Attributes
	type = models.ForeignKey(Attribute, verbose_name=_(u"Tipo de proyecto"), null=True, limit_choices_to={'type': 'project-type'}, related_name='projects_with_type')
	status = models.ForeignKey(Attribute, verbose_name=_(u"Estado del proyecto"), null=True, limit_choices_to={'type': 'project-status'}, related_name='projects_with_status')
	kam = models.ForeignKey(Attribute, verbose_name=_(u"KAM del proyecto"), null=True, limit_choices_to={'type': 'project-kam'}, related_name='projects_with_kam')
	admin = models.ForeignKey(Attribute, verbose_name=_(u"Administrador del proyecto"),  null=True, limit_choices_to={'type': 'project-admin'}, related_name='projects_with_admin')
	rd = models.ForeignKey(Attribute, verbose_name=_(u"RD del proyecto"), null=True,  limit_choices_to={'type': 'project-rd'}, related_name='projects_with_rd')
	client = models.ForeignKey(Attribute, verbose_name=_(u"Cliente"),  null=True, limit_choices_to={'type': 'project-client'}, related_name='projects_with_client')

	#Services
	services = models.ManyToManyField(Service, related_name="services", verbose_name=_("Servicios"))

	objects = models.Manager()
	total = TotalManager()


	def __unicode__(self):
		return self.name

	def __str__(self):
		return self.name

	def __repr__(self):
		return "<Project {0}>".format(self.id)
	
	def save(self, *args, **kwargs):
		if self.date_modified:
			self.date_modified = timezone.now()
		super(Project, self).save(*args, **kwargs)

	def get_roles(self):
		return self.roles.all()

	def get_type(self):
		return self.filter(id=self.id).type

	def get_users(self):
		user_model = get_user_model()
		members = self.memberships.values_list("user", flat=True)
		return user_model.objects.filter(id__in=list(members))	

	def get_risk_totals(self, year=datetime.now().isocalendar()[0], week=datetime.now().isocalendar()[1]):
		tsk_com = TaskList.objects.filter(project=self.id, name=('Semana %d %d' % (week, year))) \
									.filter(tsk_item__completed=True) \
									.aggregate(completed=Count('tsk_item'))
		tsk_incom = TaskList.objects.filter(project=self.id, name=('Semana %d %d' % (week, year))) \
									.filter(tsk_item__completed=False) \
									.aggregate(incompleted=Count('tsk_item'))		
		tsk_total = float(tsk_com['completed']) + float(tsk_incom['incompleted'])
		
		values = {}
		values['total'] = tsk_total
		values['completed'] = tsk_com['completed']
		try:
			values['percent'] = (float(tsk_com['completed']) / tsk_total ) * 100
		except (ValueError, TypeError, ZeroDivisionError):
			values['percent'] = 0  

		return values

	def get_memberships(self):
		class MembersLists: pass
		ml = []
		membs = self.memberships.all().order_by('role','user')
		for mbs_obj in membs:
			ml_elem = MembersLists()
			ml_elem.user = mbs_obj.user.get_full_name
			ml_elem.role = mbs_obj.role
			ml_elem.tasks = None
			ml.append(ml_elem)
		return ml


	class Meta:
		verbose_name = 'proyecto'
		verbose_name_plural = 'proyectos'
		app_label = string_with_title('bt', u'Módulos')
		ordering = ('name', 'status', 'type',)

class Comment(models.Model):
	"""
	Not using Django's built-in comments because we want to be able to save
	a comment and change task details at the same time. Rolling our own since it's easy.
	"""

	author = models.ForeignKey(User, verbose_name=_(u'Autor'), blank=True)
	project = models.ForeignKey(Project, null=True,  blank=False, verbose_name=_(u'Proyecto'))
	submit_date = models.DateTimeField(default=timezone.now,  verbose_name=_(u'Fecha'))
	body = models.TextField(blank=False, verbose_name=_(u'Mensaje'))


	def __unicode__(self):
		return '%s - %s' % (
			self.author,
			self.submit_date,
		)

	class Meta:
		verbose_name = 'comentario'
		verbose_name_plural = 'comentarios'        
		app_label = string_with_title('bt', u'Módulos')    		