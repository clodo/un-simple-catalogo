from django.conf import settings
from django.core.mail import send_mail, EmailMessage
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.template.response import TemplateResponse
from django.shortcuts import get_object_or_404
from django.http import Http404

from .models import (Producto, Carrito, Comprador,) 
from .forms import CompradorForm

from django.core.files.storage import default_storage

def carrito(request):
    carrito = Carrito.objects.from_request(request, create = True)
    return TemplateResponse(request, 'carritos/carrito.html', {'carrito':carrito})

def checkout(request):
    carrito = Carrito.objects.from_request(request, create = True)
    if request.method == 'POST':
        form = CompradorForm(request.POST)
        if form.is_valid():
            comprador = form.save()
            carrito.hacer_pedido(comprador)
            carrito.save()

            # EMAIL
            # Comprador
            body = render_to_string('carritos/checkout_email.html', {'carrito': carrito})
            subject = 'Agora Hogar // Pedido'
            msg = EmailMessage(subject, body, settings.EMAIL_HOST_USER, [comprador.email])
            msg.content_subtype = "html"
            msg.send()

            # Admin
            body = render_to_string('carritos/email_admin.html', {'carrito': carrito, 'comprador': comprador})
            subject = 'Agora Hogar // Pedido'
            msg = EmailMessage(subject, body, settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER])
            msg.content_subtype = "html"
            msg.send()

            del request.session['carrito']
            return redirect('carritos.views.checkout_gracias')

    else:
        form = CompradorForm()

    return TemplateResponse(request, 'carritos/checkout.html', {'carrito': carrito, 'form': form })

def checkout_gracias(request):
    return TemplateResponse(request, 'carritos/checkout_gracias.html')

def actualizar_cantidad(request):
    carrito = Carrito.objects.from_request(request)
    if request.POST.has_key('item_id') and request.POST.has_key('cantidad'):
        item_id = request.POST['item_id']
        cantidad = request.POST['cantidad']
        carrito.actualizar_item_cantidad(item_id, cantidad)

    return redirect('carritos.views.carrito')

def borrar_item(request):
    carrito = Carrito.objects.from_request(request)
    if request.POST.has_key('item_id'):
        item_id = request.POST['item_id']
        carrito.borrar(item_id)

    return redirect('carritos.views.carrito')

def agregar_producto(request):
    if request.POST.has_key('producto_id'):
        producto = get_object_or_404(Producto, id = request.POST['producto_id'])
        carrito = Carrito.objects.from_request(request, create = True)
        cantidad = int(request.POST['cantidad']) if request.POST.has_key('cantidad') else 1
        carrito.agregar(producto, cantidad)
        return redirect('carritos.views.carrito')
    else:
        raise Http404
