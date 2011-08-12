# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Member.id_type'
        db.add_column('cadastro_member', 'id_type', self.gf('django.db.models.fields.CharField')(default='RG', max_length=4), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Member.id_type'
        db.delete_column('cadastro_member', 'id_type')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'cadastro.bikeusagesurvey': {
            'Meta': {'object_name': 'BikeUsageSurvey'},
            'bike_usage': ('cadastro.multiselectmodelfield.MultiSelectField', [], {}),
            'city_region': ('cadastro.multiselectmodelfield.MultiSelectField', [], {'default': "''", 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'expectations': ('cadastro.multiselectmodelfield.MultiSelectField', [], {}),
            'frequency': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'member': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cadastro.Member']", 'unique': 'True'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'volunteering': ('cadastro.multiselectmodelfield.MultiSelectField', [], {})
        },
        'cadastro.member': {
            'Meta': {'object_name': 'Member'},
            'address_city': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'address_etc': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'blank': 'True'}),
            'address_state': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'address_street': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'address_zip': ('django.db.models.fields.CharField', [], {'max_length': '9'}),
            'birth': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'cpf': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'education': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_type': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'organizations': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'profession': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'receive_news': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'rg': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'sexo': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['cadastro']
