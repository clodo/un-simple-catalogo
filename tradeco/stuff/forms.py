# -*- coding: utf-8 -*-
from django import forms
from .models import Contacto

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ('nombre','email', 'telefono', 'asunto', 'consulta')

    def __init__(self, *args, **kwargs):
        super(ContactoForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].label += ' (*)'
