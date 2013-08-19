# -*- coding: utf-8 -*-
from django import template
from django.conf import settings
from ..models import Carrito

register = template.Library()

@register.inclusion_tag('carritos/menu.html', takes_context = True)
def carrito_menu(context):
    request = context['request']
    carrito = Carrito.objects.from_request(request, create = True)
    return {'carrito': carrito, 'static_url': settings.STATIC_URL}
