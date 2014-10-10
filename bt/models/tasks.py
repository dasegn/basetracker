# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from bt.models.projects import Project
from bt.models.attributes import Attribute
from utils.adminLabels import string_with_title
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext as _

import datetime

class TaskList(models.Model):
    name = models.CharField(max_length=140)
    slug = models.SlugField(max_length=140, editable=False)
    team = models.ForeignKey(Group)
    project = models.ForeignKey(Project)

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
        ordering = ["name"]
        verbose_name = 'Lista de tareas'
        verbose_name_plural = 'Listas de tareas'

        # Prevents (at the database level) creation of two lists with the same name in the same group
        unique_together = ("team", "slug")
        app_label = string_with_title('bt', u'Módulos')



class Task(models.Model):
    title = models.CharField(max_length=140)
    description = models.TextField(null=False, blank=True, verbose_name=_("descripcion"))
    list = models.ForeignKey(TaskList)
    created_date = models.DateField(auto_now=True, auto_now_add=True)
    due_date = models.DateField(blank=True, null=True)
    completed = models.BooleanField()
    completed_date = models.DateField(blank=True, null=True)
    created_by = models.ForeignKey(User, related_name='task_created_by')
    assigned_to = models.ForeignKey(User,  blank=True, null=True, default=None,  verbose_name=_("asignada a"), related_name='task_assigned_to')
    note = models.TextField(blank=True, null=True)

    priority = models.ForeignKey(Attribute,  null=True, limit_choices_to={'type': 'task-priority'}, related_name='task_with_priority')

    def overdue_status(self):
        "Returns whether the item's due date has passed or not."
        if self.due_date and datetime.date.today() > self.due_date:
            return 1

    def __unicode__(self):
    	return self.title

    # Auto-set the item creation / completed date
    def save(self, *args, **kwargs):
        # If Item is being marked complete, set the completed_date
        if self.completed:
            self.completed_date = datetime.datetime.now()
        super(Task, self).save()

    class Meta:
    	ordering = ['priority']
        verbose_name = 'Tarea'
        verbose_name_plural = 'Tareas'
        app_label = string_with_title('bt', u'Módulos')


class Comment(models.Model):
    """
    Not using Django's built-in comments because we want to be able to save
    a comment and change task details at the same time. Rolling our own since it's easy.
    """

    author = models.ForeignKey(User)
    tasklist = models.ForeignKey(TaskList)
    date = models.DateTimeField(default=datetime.datetime.now)
    body = models.TextField(blank=True)

    def __unicode__(self):
        return '%s - %s' % (
            self.author,
            self.date,
        )
    class Meta:
        app_label = string_with_title('bt', u'Módulos')    