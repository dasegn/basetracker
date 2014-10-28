# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from bt.models.projects import Project
from bt.models.attributes import Attribute
from bt.models.services import Service

from utils.adminLabels import string_with_title
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext as _

import datetime
from django.utils import timezone


class TaskList(models.Model):
    name = models.CharField(max_length=140, verbose_name=_(u'Nombre'))
    slug = models.SlugField(max_length=140, editable=False)
    project = models.ForeignKey(Project, verbose_name=_(u'Proyecto'))

    tstatus = models.ForeignKey(Attribute, verbose_name=_(u'Estado'), null=True, limit_choices_to={'type': 'task-status'}, related_name='task_with_status')

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)

        super(TaskList, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

    # Custom manager lets us do things like Item.completed_tasks.all()
    objects = models.Manager()

    def incomplete_tasks(self):
        # Count all incomplete tasks on the current list instance
        return Item.objects.filter(list=self, completed=0)

    class Meta:
        ordering = ["name",'tstatus']
        verbose_name = 'lista de tareas'
        verbose_name_plural = 'listas de tareas'

        # Prevents (at the database level) creation of two lists with the same name in the same group
        #unique_together = ("team", "slug")
        app_label = string_with_title('bt', u'Módulos')



class Task(models.Model):
    title = models.CharField(max_length=140, verbose_name=_(u'Titulo'))
    description = models.TextField(null=False, blank=True, default="", verbose_name=_(u'Descripción'))
    list = models.ForeignKey(TaskList)
    created_date = models.DateField(auto_now=True, auto_now_add=True, verbose_name=_(u'Fecha inicio'))
    hours = models.DecimalField(verbose_name=_(u'Horas'), max_digits=5, decimal_places=2, default=0)
    created_by = models.ForeignKey(User, blank=True, related_name='task_created_by', verbose_name=_(u'Creada por'))
    assigned_to = models.ForeignKey(User,  blank=False, null=False, default=None,  verbose_name=_("Asignada a"), related_name='task_assigned_to')

    due_date = models.DateField(blank=True, null=True, verbose_name=_(u'Fecha fin'))
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
        super(Task, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'tarea'
        verbose_name_plural = 'tareas'
        app_label = string_with_title('bt', u'Módulos')


class Comment(models.Model):
    """
    Not using Django's built-in comments because we want to be able to save
    a comment and change task details at the same time. Rolling our own since it's easy.
    """

    author = models.ForeignKey(User, verbose_name=_(u'Autor'), blank=True)
    tasklist = models.ForeignKey(TaskList, verbose_name=_(u'Lista de tareas'))
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