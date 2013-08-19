from django import forms
from .models import Comprador

class CompradorForm(forms.ModelForm):
    class Meta:
        model = Comprador
