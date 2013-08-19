# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Carrito.comprador'
        db.alter_column(u'carritos_carrito', 'comprador_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['carritos.Comprador'], null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Carrito.comprador'
        raise RuntimeError("Cannot reverse this migration. 'Carrito.comprador' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Carrito.comprador'
        db.alter_column(u'carritos_carrito', 'comprador_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['carritos.Comprador']))

    models = {
        u'carritos.carrito': {
            'Meta': {'object_name': 'Carrito'},
            'checkout': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'comprador': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['carritos.Comprador']", 'null': 'True', 'blank': 'True'}),
            'fecha_checkout': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'fecha_creacion': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'carritos.carritoitem': {
            'Meta': {'object_name': 'CarritoItem'},
            'cantidad': ('django.db.models.fields.IntegerField', [], {}),
            'carrito': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['carritos.Carrito']"}),
            'fecha_creacion': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'precio_checkout': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'producto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['productos.Producto']"})
        },
        u'carritos.comprador': {
            'Meta': {'object_name': 'Comprador'},
            'apellido': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'productos.categoria': {
            'Meta': {'object_name': 'Categoria'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'})
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
            'precio': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'sub_categoria': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': u"orm['productos.SubCategoria']", 'null': 'True', 'blank': 'True'}),
            'titulo': ('django.db.models.fields.TextField', [], {'max_length': '50'})
        },
        u'productos.subcategoria': {
            'Meta': {'object_name': 'SubCategoria'},
            'categoria': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['productos.Categoria']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'})
        }
    }

    complete_apps = ['carritos']