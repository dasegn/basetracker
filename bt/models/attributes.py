#-*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext as _
from utils.adminLabels import string_with_title

class Attribute(models.Model):
	PROJECT_TYPE = 'project-type'
	PROJECT_STATUS = 'project-status'
    ATTRIBUTE_TYPES = {
        PROJECT_TYPE: 'Tipo de proyecto',
        PROJECT_STATUS: 'Estado del proyecto',
        PROJECT_KAM: 'KAM del proyecto',
        PROJECT_ADMIN: 'Administrador de proyecto',
        PROJECT_RD: 'Responsable de diseño',
        PROJECT_CLIENT: 'Cliente',
    }
    type = models.CharField(max_length=32, choices=ATTRIBUTE_TYPES.items())
    label = models.CharField(max_length=255)

    class Meta:
        db_table = 'bt_attribute'  # Using legacy table name.
        verbose_name = 'Atributo'
        verbose_name_plural = 'Atributos'        
        unique_together = ('type', 'label')
        app_label = string_with_title('bt', u'Módulos')


    def __unicode__(self):
        return self.label
