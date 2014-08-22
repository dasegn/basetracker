# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Project'
        db.create_table(u'projects_project', (
            ('id', self.gf('django.db.models.fields.AutoField')(unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('identifier', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['projects.Project'], null=True, blank=True)),
            ('access', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('date_begin', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('date_end', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('status', self.gf('django.db.models.fields.IntegerField')(default=1)),
        ))
        db.send_create_signal(u'projects', ['Project'])


    def backwards(self, orm):
        # Deleting model 'Project'
        db.delete_table(u'projects_project')


    models = {
        u'projects.project': {
            'Meta': {'object_name': 'Project'},
            'access': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'date_begin': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'date_end': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'unique': 'True', 'primary_key': 'True'}),
            'identifier': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'default': '0', 'to': u"orm['projects.Project']", 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        }
    }

    complete_apps = ['projects']