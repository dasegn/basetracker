# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Project.date_begin'
        db.alter_column(u'projects_project', 'date_begin', self.gf('django.db.models.fields.DateTimeField')(null=True))

        # Renaming column for 'Project.parent' to match new field type.
        db.rename_column(u'projects_project', 'parent', 'parent_id')
        # Changing field 'Project.parent'
        db.alter_column(u'projects_project', 'parent_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projects.Project'], null=True))
        # Adding index on 'Project', fields ['parent']
        db.create_index(u'projects_project', ['parent_id'])


        # Changing field 'Project.date_end'
        db.alter_column(u'projects_project', 'date_end', self.gf('django.db.models.fields.DateTimeField')(null=True))

    def backwards(self, orm):
        # Removing index on 'Project', fields ['parent']
        db.delete_index(u'projects_project', ['parent_id'])


        # Changing field 'Project.date_begin'
        db.alter_column(u'projects_project', 'date_begin', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True))

        # Renaming column for 'Project.parent' to match new field type.
        db.rename_column(u'projects_project', 'parent_id', 'parent')
        # Changing field 'Project.parent'
        db.alter_column(u'projects_project', 'parent', self.gf('django.db.models.fields.IntegerField')(default=0))

        # Changing field 'Project.date_end'
        db.alter_column(u'projects_project', 'date_end', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True))

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
            'status': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['projects']