# -*- coding: utf-8 -*-
from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import Resize

class Banner(models.Model):
    orden = models.PositiveIntegerField()
    imagen = models.ImageField(upload_to='banners')
    home = ImageSpecField([Resize(920, 300)], source='imagen')

class Contacto(models.Model):
    nombre = models.CharField(max_length = 100)
    email = models.EmailField()
    telefono = models.CharField("Teléfono", max_length = 50, blank = True, null = True)
    asunto = models.CharField(max_length = 200)
    consulta = models.TextField()
    fecha = models.DateTimeField(auto_now_add = True)
