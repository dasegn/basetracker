# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Team'
        db.create_table(u'teams_team', (
            ('id', self.gf('django.db.models.fields.AutoField')(unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'teams', ['Team'])

        # Adding M2M table for field projects on 'Team'
        m2m_table_name = db.shorten_name(u'teams_team_projects')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('team', models.ForeignKey(orm[u'teams.team'], null=False)),
            ('project', models.ForeignKey(orm[u'projects.project'], null=False))
        ))
        db.create_unique(m2m_table_name, ['team_id', 'project_id'])


    def backwards(self, orm):
        # Deleting model 'Team'
        db.delete_table(u'teams_team')

        # Removing M2M table for field projects on 'Team'
        db.delete_table(db.shorten_name(u'teams_team_projects'))


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
        },
        u'teams.team': {
            'Meta': {'object_name': 'Team'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'unique': 'True', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'projects': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['projects.Project']", 'symmetrical': 'False'})
        }
    }

    complete_apps = ['teams']