from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit
from smart_selects.db_fields import ChainedForeignKey 

class Categoria(models.Model):
    nombre = models.CharField('Categoria', max_length = 100)
    categoria = models.Manager()

    def __unicode__(self):
        return self.nombre

class SubCategoria(models.Model):
    categoria = models.ForeignKey(Categoria)
    nombre = models.CharField('Sub Categoria', max_length = 100)

    def __unicode__(self):
        return self.nombre

class ProductoDestacadoManager(models.Manager):
    def get_query_set(self):
        return super(ProductoDestacadoManager, self).get_query_set() \
                .filter(destacado__isnull = False).order_by('destacado')

class Producto(models.Model):
    codigo = models.TextField(max_length = 30, blank = True, null = True)
    titulo = models.TextField(max_length = 50)
    categoria = models.ForeignKey(Categoria)
    sub_categoria = ChainedForeignKey(
            SubCategoria, 
            chained_field="categoria",
            chained_model_field="categoria", 
            show_all=False, 
            auto_choose=True, 
            blank = True, 
            null = True
    )
    descripcion = models.TextField(max_length = 250)
    destacado = models.PositiveIntegerField('Destacado Orden', blank = True, null = True)
    created_at = models.DateTimeField(auto_now_add = True)
    modified_at = models.DateTimeField(auto_now = True)

    producto = models.Manager()
    destacados = ProductoDestacadoManager()

    def thumbnail(self):
        return self.productoimagen_set.order_by('id')[0].thumbnail if len(self.productoimagen_set.all()) else None

    def __unicode__(self):
        return self.descripcion

class ProductoImagen(models.Model):
    producto = models.ForeignKey(Producto)
    imagen = models.ImageField(upload_to='productos')
    thumbnail = ImageSpecField([ResizeToFit(152, 152)], source='imagen', options={'quality':60})
    detalle = ImageSpecField([ResizeToFit(320, 430)], source='imagen')

    def __unicode__(self):
        return '{0}:'.format(self.id)
