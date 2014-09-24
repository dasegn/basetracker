# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Attribute'
        db.create_table('bt_attribute', (
            ('id', self.gf('django.db.models.fields.AutoField')(unique=True, primary_key=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('bt', ['Attribute'])

        # Adding unique constraint on 'Attribute', fields ['type', 'label']
        db.create_unique('bt_attribute', ['type', 'label'])

        # Adding field 'Project.type'
        db.add_column(u'bt_project', 'type',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='projects_with_type', null=True, to=orm['bt.Attribute']),
                      keep_default=False)

        # Adding field 'Project.kam'
        db.add_column(u'bt_project', 'kam',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='projects_with_kam', null=True, to=orm['bt.Attribute']),
                      keep_default=False)

        # Adding field 'Project.admin'
        db.add_column(u'bt_project', 'admin',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='projects_with_admin', null=True, to=orm['bt.Attribute']),
                      keep_default=False)

        # Adding field 'Project.rd'
        db.add_column(u'bt_project', 'rd',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='projects_with_rd', null=True, to=orm['bt.Attribute']),
                      keep_default=False)

        # Adding field 'Project.client'
        db.add_column(u'bt_project', 'client',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='projects_with_client', null=True, to=orm['bt.Attribute']),
                      keep_default=False)

        # Adding M2M table for field groups on 'Project'
        m2m_table_name = db.shorten_name(u'bt_project_groups')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm['bt.project'], null=False)),
            ('group', models.ForeignKey(orm[u'auth.group'], null=False))
        ))
        db.create_unique(m2m_table_name, ['project_id', 'group_id'])


        # Renaming column for 'Project.status' to match new field type.
        db.rename_column(u'bt_project', 'status', 'status_id')
        # Changing field 'Project.status'
        db.alter_column(u'bt_project', 'status_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['bt.Attribute']))
        # Adding index on 'Project', fields ['status']
        db.create_index(u'bt_project', ['status_id'])


    def backwards(self, orm):
        # Removing index on 'Project', fields ['status']
        db.delete_index(u'bt_project', ['status_id'])

        # Removing unique constraint on 'Attribute', fields ['type', 'label']
        db.delete_unique('bt_attribute', ['type', 'label'])

        # Deleting model 'Attribute'
        db.delete_table('bt_attribute')

        # Deleting field 'Project.type'
        db.delete_column(u'bt_project', 'type_id')

        # Deleting field 'Project.kam'
        db.delete_column(u'bt_project', 'kam_id')

        # Deleting field 'Project.admin'
        db.delete_column(u'bt_project', 'admin_id')

        # Deleting field 'Project.rd'
        db.delete_column(u'bt_project', 'rd_id')

        # Deleting field 'Project.client'
        db.delete_column(u'bt_project', 'client_id')

        # Removing M2M table for field groups on 'Project'
        db.delete_table(db.shorten_name(u'bt_project_groups'))


        # Renaming column for 'Project.status' to match new field type.
        db.rename_column(u'bt_project', 'status_id', 'status')
        # Changing field 'Project.status'
        db.alter_column(u'bt_project', 'status', self.gf('django.db.models.fields.IntegerField')())

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
            'id': ('django.db.models.fields.AutoField', [], {'unique': 'True', 'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '32'})
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
            'access': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'admin': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'projects_with_admin'", 'null': 'True', 'to': "orm['bt.Attribute']"}),
            'client': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'projects_with_client'", 'null': 'True', 'to': "orm['bt.Attribute']"}),
            'date_begin': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'date_end': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'unique': 'True', 'primary_key': 'True'}),
            'identifier': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'kam': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'projects_with_kam'", 'null': 'True', 'to': "orm['bt.Attribute']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'default': '0', 'to': "orm['bt.Project']", 'null': 'True', 'blank': 'True'}),
            'rd': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'projects_with_rd'", 'null': 'True', 'to': "orm['bt.Attribute']"}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'projects_with_status'", 'null': 'True', 'to': "orm['bt.Attribute']"}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'projects_with_type'", 'null': 'True', 'to': "orm['bt.Attribute']"}),
            'users': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.User']", 'symmetrical': 'False'})
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