# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Attribute'
        db.create_table(u'bt_attribute', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('bt', ['Attribute'])

        # Adding unique constraint on 'Attribute', fields ['type', 'label']
        db.create_unique(u'bt_attribute', ['type', 'label'])

        # Adding model 'Project'
        db.create_table(u'bt_project', (
            ('id', self.gf('django.db.models.fields.AutoField')(unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')(default='')),
            ('identifier', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['bt.Project'], blank=True)),
            ('access', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('date_begin', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('date_end', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('date_modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='projects_with_type', null=True, to=orm['bt.Attribute'])),
            ('status', self.gf('django.db.models.fields.related.ForeignKey')(related_name='projects_with_status', null=True, to=orm['bt.Attribute'])),
            ('kam', self.gf('django.db.models.fields.related.ForeignKey')(related_name='projects_with_kam', null=True, to=orm['bt.Attribute'])),
            ('admin', self.gf('django.db.models.fields.related.ForeignKey')(related_name='projects_with_admin', null=True, to=orm['bt.Attribute'])),
            ('rd', self.gf('django.db.models.fields.related.ForeignKey')(related_name='projects_with_rd', null=True, to=orm['bt.Attribute'])),
            ('client', self.gf('django.db.models.fields.related.ForeignKey')(related_name='projects_with_client', null=True, to=orm['bt.Attribute'])),
        ))
        db.send_create_signal('bt', ['Project'])

        # Adding M2M table for field users on 'Project'
        m2m_table_name = db.shorten_name(u'bt_project_users')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm['bt.project'], null=False)),
            ('user', models.ForeignKey(orm[u'auth.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['project_id', 'user_id'])

        # Adding M2M table for field groups on 'Project'
        m2m_table_name = db.shorten_name(u'bt_project_groups')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm['bt.project'], null=False)),
            ('group', models.ForeignKey(orm[u'auth.group'], null=False))
        ))
        db.create_unique(m2m_table_name, ['project_id', 'group_id'])

        # Adding model 'Team'
        db.create_table(u'bt_team', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('group', self.gf('django.db.models.fields.related.OneToOneField')(related_name='Team', unique=True, to=orm['auth.Group'])),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('bt', ['Team'])

        # Adding M2M table for field members on 'Team'
        m2m_table_name = db.shorten_name(u'bt_team_members')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('team', models.ForeignKey(orm['bt.team'], null=False)),
            ('user', models.ForeignKey(orm[u'auth.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['team_id', 'user_id'])

        # Adding model 'Profile'
        db.create_table(u'bt_profile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(related_name='profile', unique=True, to=orm['auth.User'])),
            ('hours_per_week', self.gf('django.db.models.fields.DecimalField')(default=30, max_digits=8, decimal_places=2)),
            ('skype', self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True)),
            ('avatar', self.gf('django.db.models.fields.files.ImageField')(default='', max_length=100, blank=True)),
        ))
        db.send_create_signal('bt', ['Profile'])

        # Adding model 'TaskList'
        db.create_table(u'bt_tasklist', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=140)),
            ('team', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.Group'])),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bt.Project'])),
        ))
        db.send_create_signal('bt', ['TaskList'])

        # Adding unique constraint on 'TaskList', fields ['team', 'slug']
        db.create_unique(u'bt_tasklist', ['team_id', 'slug'])

        # Adding model 'Task'
        db.create_table(u'bt_task', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('description', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('list', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bt.TaskList'])),
            ('created_date', self.gf('django.db.models.fields.DateField')(auto_now=True, auto_now_add=True, blank=True)),
            ('due_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('completed', self.gf('django.db.models.fields.BooleanField')()),
            ('completed_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='task_created_by', to=orm['auth.User'])),
            ('assigned_to', self.gf('django.db.models.fields.related.ForeignKey')(default=None, related_name='task_assigned_to', blank=True, to=orm['auth.User'])),
            ('note', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('priority', self.gf('django.db.models.fields.related.ForeignKey')(related_name='task_with_priority', null=True, to=orm['bt.Attribute'])),
        ))
        db.send_create_signal('bt', ['Task'])

        # Adding model 'Comment'
        db.create_table(u'bt_comment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('tasklist', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bt.TaskList'])),
            ('date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('body', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('bt', ['Comment'])


    def backwards(self, orm):
        # Removing unique constraint on 'TaskList', fields ['team', 'slug']
        db.delete_unique(u'bt_tasklist', ['team_id', 'slug'])

        # Removing unique constraint on 'Attribute', fields ['type', 'label']
        db.delete_unique(u'bt_attribute', ['type', 'label'])

        # Deleting model 'Attribute'
        db.delete_table(u'bt_attribute')

        # Deleting model 'Project'
        db.delete_table(u'bt_project')

        # Removing M2M table for field users on 'Project'
        db.delete_table(db.shorten_name(u'bt_project_users'))

        # Removing M2M table for field groups on 'Project'
        db.delete_table(db.shorten_name(u'bt_project_groups'))

        # Deleting model 'Team'
        db.delete_table(u'bt_team')

        # Removing M2M table for field members on 'Team'
        db.delete_table(db.shorten_name(u'bt_team_members'))

        # Deleting model 'Profile'
        db.delete_table(u'bt_profile')

        # Deleting model 'TaskList'
        db.delete_table(u'bt_tasklist')

        # Deleting model 'Task'
        db.delete_table(u'bt_task')

        # Deleting model 'Comment'
        db.delete_table(u'bt_comment')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'bt.attribute': {
            'Meta': {'unique_together': "(('type', 'label'),)", 'object_name': 'Attribute'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        'bt.comment': {
            'Meta': {'object_name': 'Comment'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'body': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tasklist': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bt.TaskList']"})
        },
        'bt.profile': {
            'Meta': {'object_name': 'Profile'},
            'avatar': ('django.db.models.fields.files.ImageField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'hours_per_week': ('django.db.models.fields.DecimalField', [], {'default': '30', 'max_digits': '8', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'skype': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'profile'", 'unique': 'True', 'to': u"orm['auth.User']"})
        },
        'bt.project': {
            'Meta': {'ordering': "('name', 'status', 'type')", 'object_name': 'Project'},
            'access': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'admin': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'projects_with_admin'", 'null': 'True', 'to': "orm['bt.Attribute']"}),
            'client': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'projects_with_client'", 'null': 'True', 'to': "orm['bt.Attribute']"}),
            'date_begin': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'date_end': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'unique': 'True', 'primary_key': 'True'}),
            'identifier': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'kam': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'projects_with_kam'", 'null': 'True', 'to': "orm['bt.Attribute']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'default': '0', 'to': "orm['bt.Project']", 'blank': 'True'}),
            'rd': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'projects_with_rd'", 'null': 'True', 'to': "orm['bt.Attribute']"}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'projects_with_status'", 'null': 'True', 'to': "orm['bt.Attribute']"}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'projects_with_type'", 'null': 'True', 'to': "orm['bt.Attribute']"}),
            'users': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'projects'", 'symmetrical': 'False', 'to': u"orm['auth.User']"})
        },
        'bt.task': {
            'Meta': {'ordering': "['priority']", 'object_name': 'Task'},
            'assigned_to': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'task_assigned_to'", 'blank': 'True', 'to': u"orm['auth.User']"}),
            'completed': ('django.db.models.fields.BooleanField', [], {}),
            'completed_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'task_created_by'", 'to': u"orm['auth.User']"}),
            'created_date': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'due_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'list': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bt.TaskList']"}),
            'note': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'priority': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'task_with_priority'", 'null': 'True', 'to': "orm['bt.Attribute']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '140'})
        },
        'bt.tasklist': {
            'Meta': {'ordering': "['name']", 'unique_together': "(('team', 'slug'),)", 'object_name': 'TaskList'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bt.Project']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '140'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.Group']"})
        },
        'bt.team': {
            'Meta': {'object_name': 'Team'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'group': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'Team'", 'unique': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'members': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.User']", 'symmetrical': 'False'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['bt']