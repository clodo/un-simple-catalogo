import json 

from django.conf import settings
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.mail import send_mail, EmailMessage
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.template.response import TemplateResponse
from django.shortcuts import get_object_or_404
from django.http import Http404

from models import (Producto, Carrito,) 

from django.core.files.storage import default_storage

def carrito(request):
    carrito = Carrito.objects.from_request(request, create = True)
    template = 'carritos/carrito.html'
    if request.is_ajax():
        template = 'carritos/_carrito_items.html'

        if request.POST.has_key('item-id'):
            items_ids = request.POST.getlist('item-id')

            if request.POST.has_key('cantidad-item'): 
                items_cantidad = request.POST.getlist('cantidad-item')
                for i in range(len(items_ids)):
                    carrito.actualizar_item_cantidad(items_ids[i], items_cantidad[i])

    return TemplateResponse(request, template, {'carrito':carrito})

@login_required
def carrito_checkout(request):
    carrito = Carrito.objects.from_request(request, create = True)
    if not carrito.es_valido():
        return redirect('carritos.views.carrito')

    checkout = True
    template = 'carritos/carrito.html'
    items_per_negocios = carrito.items_per_negocios()
    if request.method == 'POST':
        carrito.hacer_pedido()
        carrito.save()

        # EMAIL
        body = render_to_string('carritos/checkout_email_comprador.html', 
                {'items_per_negocios': items_per_negocios})

        subject = 'Mas Avellaneda // Comprador // Checkout'
        msg = EmailMessage(subject, body, settings.EMAIL_HOST_USER, [request.user.email])

        msg.content_subtype = "html"
        msg.send()

        #  - Admin
        body = render_to_string('carritos/checkout_email_admin.html', 
                {'items_per_negocios': items_per_negocios, 'comprador':request.user })
        subject = 'Mas Avellaneda // Carrito // Checkout'
        msg = EmailMessage(subject, body, settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER])
        msg.content_subtype = "html"
        msg.send()

        checkout = False
        template = 'carritos/checkout_gracias.html'

    return TemplateResponse(request, template,
            {'carrito': carrito, 'checkout' : checkout, 'detalle': True,'items_per_negocios': items_per_negocios })

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
