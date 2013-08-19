# -*- coding: utf-8 -*-
from django import template

register = template.Library()

@register.inclusion_tag('carritos/menu.html')
def carrito_menu():
    return {'banners': None}
