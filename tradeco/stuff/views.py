from django.conf import settings
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from django.shortcuts import redirect
from django.template.response import TemplateResponse

from .forms import ContactoForm

def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            contacto = form.save()

            body = render_to_string('stuff/contacto_email.html', {'base_url': settings.BASE_URL, 'contacto': contacto })
            subject = 'Agora Hogar // Contacto'
            msg = EmailMessage(subject, body, settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER], headers = {'Reply-To': form.cleaned_data.get('email')})
            msg.content_subtype = "html"
            msg.send()

            return redirect('stuff.views.contacto_gracias')
    else:
        form = ContactoForm()

    return TemplateResponse(request, 'stuff/contacto.html', { 'form':form })

def contacto_gracias(request):
    return TemplateResponse(request, 'stuff/contacto_gracias.html')
