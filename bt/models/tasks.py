# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.db.models import Count, Min, Sum, Avg

from bt.models.projects import Project
from bt.models.attributes import Attribute
from bt.models.services import Service
from bt.models.membership import Membership

from utils.adminLabels import string_with_title
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext as _
from django.core.exceptions import ValidationError
from smart_selects.db_fields import ChainedForeignKey 

import datetime

class TaskList(models.Model):
    name = models.CharField(max_length=140, verbose_name=_(u'Nombre'))
    slug = models.SlugField(max_length=140, editable=False)
    project = models.ForeignKey(Project, null=False, blank=False, verbose_name=_(u'Proyecto'))
    service = ChainedForeignKey(Service, chained_field="project", chained_model_field="services", null=False, blank=False, verbose_name=_(u'Servicio'))
    list_start = models.DateField(null=True, blank=False, verbose_name=_(u'Fecha de inicio'))  
    list_end =  models.DateField(null=True, blank=False, verbose_name=_(u'Fecha de fin'))  
    list_created = models.DateTimeField(auto_now_add=True)
    list_modified = models.DateTimeField(auto_now=True)


    def save(self, *args, **kwargs):
        if not self.id:
            if not self.list_created:
                self.list_created = datetime.datetime.today()
            if not self.list_modified:
                self.list_modified = datetime.datetime.today()
        else:
            self.list_modified = datetime.datetime.today()

        if not self.id:
            self.slug = slugify(self.name)
        super(TaskList, self).save(*args, **kwargs)


    def clean(self):
        tasklist = TaskList.objects.filter(name=self.name, project=self.project, service=self.service)        
        if tasklist.count() > 0 and tasklist[0].id != self.id:
            raise ValidationError(_('La lista de tareas de esa semana, proyecto y servicio ya existe!'))

    def __str__(self):
        return unicode(self.name)

    def __unicode__(self):
        return unicode(self.name)

    # Custom manager lets us do things like Item.completed_tasks.all()
    objects = models.Manager()

    def incomplete_tasks(self):
        # Count all incomplete tasks on the current list instance
        return TaskList.objects.filter(list=self, completed=0)

    def count_tasks(self):
        return u'%s' % TaskList.objects.get(id=self.id).task_set.all().count()

    def count_hours(self):
        total_hours = TaskList.objects.annotate(hours=Sum('tasklistsummary__hours')).filter(pk=self.id)
        return u'%d' % (total_hours[0].hours)

    def progress_tasks(self):
        tasks = TaskList.objects.get(id=self.id).task_set.all()
        try:
            return u"%d%%" % (float(tasks.filter(completed=True).count()) / tasks.count() * 100)
        except (ValueError, ZeroDivisionError):
            return u""
    
    def count_members_tasks(self):
        return TaskList.objects.get(id=self.id).tasklistsummary_set.all().count()

    def get_tasks(self):
        return TaskList.objects.get(id=self.id).task_set.all().order_by('completed')

    def risk_color_tasks(self):
        try:
            progress = int(self.progress_tasks().strip('%'))
        except(ValueError):
            return 'primary'

        if progress >= 0 and progress <= 50:
            return 'danger'
        elif progress >= 51 and progress <= 75:
            return 'warning'
        elif progress >= 76 and progress <= 100:
            return 'successful'
        else:
            return 'primary'


    def week_number(self):
        if self.id:
            if isinstance(self.list_start, datetime.date):               
                return u'%s' % self.list_start.isocalendar()[1]
        else:
            return u""



    count_tasks.short_description = 'Tareas'
    progress_tasks.allow_tags = True
    progress_tasks.short_description = 'Progreso'
    week_number.short_description = 'Semana'

    class Meta:
        ordering = ["name",'project']
        verbose_name = 'lista de tareas'
        verbose_name_plural = 'listas de tareas'

        # Prevents (at the database level) creation of two lists with the same name in the same group
        #unique_together = ("team", "slug")
        app_label = string_with_title('bt', u'Módulos')



class Task(models.Model):
    title = models.CharField(max_length=140, null=False, verbose_name=_(u'Titulo'))
    description = models.TextField(null=False, blank=True, default="", verbose_name=_(u'Descripción'))
    list = models.ForeignKey(TaskList)
    created_by = models.ForeignKey(User, null=True, blank=True, default=None, related_name='task_created_by', verbose_name=_(u'Creada por'))

    created_date = models.DateField(auto_now=True, auto_now_add=True, verbose_name=_(u'Fecha de creación'))    
    completed_date = models.DateField(blank=True, null=True, verbose_name=_(u'Fecha de completado'))
    completed = models.BooleanField(verbose_name=_(u'Completado'))

    def overdue_status(self):
        "Returns whether the item's due date has passed or not."
        if self.due_date and datetime.date.today() > self.due_date:
            return 1

    def __unicode__(self):
    	return self.title

    def __str__(self):
        return "({1}) {0}".format(self.title, self.description)

    # Auto-set the item creation / completed date
    def save(self, *args, **kwargs):
        # If Item is being marked complete, set the completed_date
        if self.completed:
            self.completed_date = datetime.datetime.now()
        if self.pk:
            self.created_date = datetime.datetime.now()
        super(Task, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'tarea'
        verbose_name_plural = 'tareas'
        app_label = string_with_title('bt', u'Módulos')


class TaskListSummary(models.Model):
    list = models.ForeignKey(TaskList)
    assigned = models.ForeignKey(Membership,  blank=False, null=False, default=None,  verbose_name=_(u"Asignada a"), related_name='tasklist_assigned_to')
    hours = models.DecimalField(verbose_name=_(u'Horas'), max_digits=5, decimal_places=2, default=0)

    def __unicode__(self):
        return u'(%s) {%d}' % (self.assigned.user, self.hours)

    def __str__(self):
        return u'(%s) {%d}' % (self.assigned.user, self.hours)


#    def clean(self):
#        membership = Membership.objects.get(id=self.assigned, project=self.project)        
#        if tasklist.count() > 0 and tasklist[0].id != self.id:
#            raise ValidationError(_('La lista de tareas de esa semana, proyecto y servicio ya existe!'))
        
    class Meta:
        verbose_name = 'detalle de lista'
        verbose_name_plural = 'detalles de listas'
        app_label = string_with_title('bt', u'Módulos')

