from django.contrib import admin
from .models import (Categoria, SubCategoria, ProductoImagen, Producto,)


class CategoriaAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("nombre",)}

class SubCategoriaAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("nombre",)}

class ProductoImagenInline(admin.StackedInline):
    model = ProductoImagen
    verbose_name = 'Imagen'
    verbose_name_plural = 'Imagenes'
    extra = 2
    max_num = 7

class ProductoAdmin(admin.ModelAdmin):
    model = Producto
    prepopulated_fields = {"slug": ("titulo", "codigo")}
    inlines = (ProductoImagenInline, )
    list_filter = ('categoria__nombre', 'codigo')
    list_display = ('codigo', 'categoria', 'titulo', )

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(SubCategoria, SubCategoriaAdmin)
admin.site.register(Producto, ProductoAdmin)
