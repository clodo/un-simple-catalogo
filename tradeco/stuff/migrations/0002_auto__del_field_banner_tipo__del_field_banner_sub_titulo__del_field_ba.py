# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Banner.tipo'
        db.delete_column(u'stuff_banner', 'tipo')

        # Deleting field 'Banner.sub_titulo'
        db.delete_column(u'stuff_banner', 'sub_titulo')

        # Deleting field 'Banner.titulo'
        db.delete_column(u'stuff_banner', 'titulo')


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Banner.tipo'
        raise RuntimeError("Cannot reverse this migration. 'Banner.tipo' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Banner.tipo'
        db.add_column(u'stuff_banner', 'tipo',
                      self.gf('django.db.models.fields.IntegerField')(),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Banner.sub_titulo'
        raise RuntimeError("Cannot reverse this migration. 'Banner.sub_titulo' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Banner.sub_titulo'
        db.add_column(u'stuff_banner', 'sub_titulo',
                      self.gf('django.db.models.fields.TextField')(max_length=30),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Banner.titulo'
        raise RuntimeError("Cannot reverse this migration. 'Banner.titulo' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Banner.titulo'
        db.add_column(u'stuff_banner', 'titulo',
                      self.gf('django.db.models.fields.TextField')(max_length=30),
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
            'apellido': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
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