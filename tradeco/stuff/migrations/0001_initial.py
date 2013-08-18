# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Banner'
        db.create_table(u'stuff_banner', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('orden', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('imagen', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('titulo', self.gf('django.db.models.fields.TextField')(max_length=30)),
            ('sub_titulo', self.gf('django.db.models.fields.TextField')(max_length=30)),
            ('tipo', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'stuff', ['Banner'])

        # Adding model 'Contacto'
        db.create_table(u'stuff_contacto', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('apellido', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('asunto', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('consulta', self.gf('django.db.models.fields.TextField')()),
            ('fecha', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'stuff', ['Contacto'])


    def backwards(self, orm):
        # Deleting model 'Banner'
        db.delete_table(u'stuff_banner')

        # Deleting model 'Contacto'
        db.delete_table(u'stuff_contacto')


    models = {
        u'stuff.banner': {
            'Meta': {'object_name': 'Banner'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'orden': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'sub_titulo': ('django.db.models.fields.TextField', [], {'max_length': '30'}),
            'tipo': ('django.db.models.fields.IntegerField', [], {}),
            'titulo': ('django.db.models.fields.TextField', [], {'max_length': '30'})
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