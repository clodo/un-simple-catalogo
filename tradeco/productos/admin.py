from django.contrib import admin
from .models import (Categoria, SubCategoria, ProductoImagen, Producto,)

class ProductoImagenInline(admin.StackedInline):
    model = ProductoImagen
    verbose_name = 'Imagen'
    verbose_name_plural = 'Imagenes'
    extra = 2
    max_num = 7

class ProductoAdmin(admin.ModelAdmin):
    model = Producto
    inlines = (ProductoImagenInline, )
    list_filter = ('categoria__nombre', 'codigo')
    list_display = ('codigo', 'categoria', 'titulo', )

admin.site.register(Categoria)
admin.site.register(SubCategoria)
admin.site.register(Producto, ProductoAdmin)
