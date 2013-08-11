# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Categoria'
        db.create_table(u'productos_categoria', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'productos', ['Categoria'])

        # Adding model 'Producto'
        db.create_table(u'productos_producto', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('codigo', self.gf('django.db.models.fields.TextField')(max_length=30, null=True, blank=True)),
            ('titulo', self.gf('django.db.models.fields.TextField')(max_length=50)),
            ('categoria', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['productos.Categoria'])),
            ('descripcion', self.gf('django.db.models.fields.TextField')(max_length=250)),
            ('destacado', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'productos', ['Producto'])

        # Adding model 'ProductoImagen'
        db.create_table(u'productos_productoimagen', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('producto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['productos.Producto'])),
            ('imagen', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'productos', ['ProductoImagen'])


    def backwards(self, orm):
        # Deleting model 'Categoria'
        db.delete_table(u'productos_categoria')

        # Deleting model 'Producto'
        db.delete_table(u'productos_producto')

        # Deleting model 'ProductoImagen'
        db.delete_table(u'productos_productoimagen')


    models = {
        u'productos.categoria': {
            'Meta': {'object_name': 'Categoria'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'productos.producto': {
            'Meta': {'object_name': 'Producto'},
            'categoria': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['productos.Categoria']"}),
            'codigo': ('django.db.models.fields.TextField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'descripcion': ('django.db.models.fields.TextField', [], {'max_length': '250'}),
            'destacado': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'titulo': ('django.db.models.fields.TextField', [], {'max_length': '50'})
        },
        u'productos.productoimagen': {
            'Meta': {'object_name': 'ProductoImagen'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'producto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['productos.Producto']"})
        }
    }

    complete_apps = ['productos']