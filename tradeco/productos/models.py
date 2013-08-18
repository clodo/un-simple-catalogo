from django.db import models
from django.db.models import Count
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit, Resize
from smart_selects.db_fields import ChainedForeignKey 

class CategoriaConProductosManager(models.Manager):
    def get_query_set(self):
        return super(CategoriaConProductosManager, self).get_query_set() \
                .annotate(productos = Count('producto')).filter(productos__gt = 0)

class Categoria(models.Model):
    nombre = models.CharField('Categoria', max_length = 100)
    categoria = models.Manager()
    slug = models.SlugField( unique=True)
    con_productos = CategoriaConProductosManager()

    def __unicode__(self):
        return self.nombre

class SubCategoria(models.Model):
    categoria = models.ForeignKey(Categoria)
    nombre = models.CharField('Sub Categoria', max_length = 100)
    slug = models.SlugField( unique=True)

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
    slug = models.SlugField(unique=True)

    producto = models.Manager()
    destacados = ProductoDestacadoManager()

    def thumbnail(self):
        return self.productoimagen_set.order_by('id')[0].thumbnail if len(self.productoimagen_set.all()) else None

    def imagenes(self):
        return self.productoimagen_set.order_by('id')

    def __unicode__(self):
        return self.descripcion

class ProductoImagen(models.Model):
    producto = models.ForeignKey(Producto)
    imagen = models.ImageField(upload_to='productos')
    thumbnail = ImageSpecField([Resize(152, 152)], source='imagen', options={'quality':60})
    detalle = ImageSpecField([Resize(350, 350)], source='imagen')
    small = ImageSpecField([Resize(62, 62)], source='imagen', options={'quality':60})

    def __unicode__(self):
        return '{0}:'.format(self.id)
