# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Contacto.apellido'
        db.delete_column(u'stuff_contacto', 'apellido')


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Contacto.apellido'
        raise RuntimeError("Cannot reverse this migration. 'Contacto.apellido' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Contacto.apellido'
        db.add_column(u'stuff_contacto', 'apellido',
                      self.gf('django.db.models.fields.CharField')(max_length=100),
                      keep_default=False)


    models = {
        u'stuff.banner': {
            'Meta': {'object_name': 'Banner'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'orden': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        u'stuff.contacto': {
            'Meta': {'object_name': 'Contacto'},
            'asunto': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'consulta': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'fecha': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['stuff']