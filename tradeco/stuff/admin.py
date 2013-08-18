from django.contrib import admin
from .models import Banner, Contacto

class ContactoAdmin(admin.ModelAdmin):
    model = Contacto
    list_display = ('fecha', 'nombre', 'email', 'telefono', 'asunto')
    list_filter = ('email', 'fecha', )

admin.site.register(Banner)
admin.site.register(Contacto, ContactoAdmin)
