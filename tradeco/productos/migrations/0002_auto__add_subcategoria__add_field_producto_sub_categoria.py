# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SubCategoria'
        db.create_table(u'productos_subcategoria', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('categoria', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['productos.Categoria'])),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'productos', ['SubCategoria'])

        # Adding field 'Producto.sub_categoria'
        db.add_column(u'productos_producto', 'sub_categoria',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['productos.SubCategoria']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'SubCategoria'
        db.delete_table(u'productos_subcategoria')

        # Deleting field 'Producto.sub_categoria'
        db.delete_column(u'productos_producto', 'sub_categoria_id')


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
            'sub_categoria': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['productos.SubCategoria']"}),
            'titulo': ('django.db.models.fields.TextField', [], {'max_length': '50'})
        },
        u'productos.productoimagen': {
            'Meta': {'object_name': 'ProductoImagen'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'producto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['productos.Producto']"})
        },
        u'productos.subcategoria': {
            'Meta': {'object_name': 'SubCategoria'},
            'categoria': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['productos.Categoria']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['productos']