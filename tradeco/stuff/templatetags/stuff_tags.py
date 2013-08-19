# -*- coding: utf-8 -*-
from django import template
from ..models import Banner

register = template.Library()

@register.inclusion_tag('stuff/banners.html')
def banners():
    banners = Banner.objects.all()
    return {'banners': banners}

