#-*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext as _
from utils.adminLabels import string_with_title

# Attribute Managers
class TypeAttributeManager(models.Manager):
    """Object manager for type attributes."""
    def get_query_set(self):
        qs = super(TypeAttributeManager, self).get_query_set()
        return qs.filter(type=Attribute.PROJECT_TYPE)

class StatusAttributeManager(models.Manager):
    """Object manager for status attributes."""
    def get_query_set(self):
        qs = super(StatusAttributeManager, self).get_query_set()
        return qs.filter(type=Attribute.PROJECT_STATUS)

class KamAttributeManager(models.Manager):
    """Object manager for status attributes."""
    def get_query_set(self):
        qs = super(KamAttributeManager, self).get_query_set()
        return qs.filter(type=Attribute.PROJECT_KAM)

class AdminAttributeManager(models.Manager):
    """Object manager for status attributes."""
    def get_query_set(self):
        qs = super(AdminAttributeManager, self).get_query_set()
        return qs.filter(type=Attribute.PROJECT_ADMIN) 

class RdAttributeManager(models.Manager):
    """Object manager for status attributes."""
    def get_query_set(self):
        qs = super(RdAttributeManager, self).get_query_set()
        return qs.filter(type=Attribute.PROJECT_RD)                   

class ClientAttributeManager(models.Manager):
    """Object manager for status attributes."""
    def get_query_set(self):
        qs = super(ClientAttributeManager, self).get_query_set()
        return qs.filter(type=Attribute.PROJECT_CLIENT)    



class Attribute(models.Model):
    PROJECT_TYPE = 'project-type'
    PROJECT_STATUS = 'project-status'
    PROJECT_KAM = 'project-kam'
    PROJECT_ADMIN = 'project-admin'
    PROJECT_RD = 'project-rd'
    PROJECT_CLIENT = 'project-client'

    ATTRIBUTE_TYPES = {
        PROJECT_TYPE: 'Tipo de proyecto',
        PROJECT_STATUS: 'Estado del proyecto',
        PROJECT_KAM: 'KAM del proyecto',
        PROJECT_ADMIN: 'Administrador de proyecto',
        PROJECT_RD: 'Responsable de diseño',
        PROJECT_CLIENT: 'Cliente',
    }

    type = models.CharField(max_length=32, choices=ATTRIBUTE_TYPES.items(), verbose_name=_(u'Tipo de atributo'))
    label = models.CharField(max_length=255, verbose_name=_(u'Valor'))

    objects = models.Manager()

    types = TypeAttributeManager()
    statuses = StatusAttributeManager()
    kams = KamAttributeManager()
    admins = AdminAttributeManager()
    rds = RdAttributeManager()
    clients = ClientAttributeManager()

    class Meta:
        #db_table = 'bt_attribute'  # Using legacy table name.
        verbose_name = 'atributo'
        verbose_name_plural = 'atributos'        
        unique_together = ('type', 'label')
        app_label = string_with_title('bt', u'Módulos')


    def __unicode__(self):
        return self.label

             