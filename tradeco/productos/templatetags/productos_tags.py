# -*- coding: utf-8 -*-
from django import template
from ..models import Categoria, Producto

register = template.Library()

@register.inclusion_tag('productos/menu_categorias.html')
def menu_categorias():
    categorias = Categoria.categoria.all()
    return {'categorias': categorias}

@register.inclusion_tag('productos/sidebar_categorias.html')
def sidebar_categorias():
    categorias = Categoria.categoria.all()
    return {'categorias': categorias}

@register.inclusion_tag('productos/productos_destacados.html')
def productos_destacados():
    destacados = Producto.destacados.all()
    return {'destacados': destacados}

@register.filter
def humanize_precio(precio):
    precio_h = str(precio).split('.')
    if len(precio_h) > 1:
        parte_entero = precio_h[0]
        parte_decimal = precio_h[1]
    else:
        parte_entero = precio_h[0]
        parte_decimal = None

    # Bue, hasta aqui llego lo horrible
    if len(parte_entero) > 6:
        parte_entero = parte_entero[:-6] + '.' + parte_entero[-6:]
        parte_entero = parte_entero[:-3] + '.' + parte_entero[-3:]
    elif len(parte_entero) > 3:
        parte_entero = parte_entero[:-3] + '.' + parte_entero[-3:]


    if parte_decimal and parte_decimal != '00':
        return "{0},{1}".format(parte_entero, parte_decimal)
    else:
        return parte_entero

