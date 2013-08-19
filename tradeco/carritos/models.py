# -*- coding: utf-8 -*-
from django.db import models
from productos.models import Producto

# https://bitbucket.org/chris1610/satchmo/wiki/Home
class CarritoManager(models.Manager):
    def from_request(self, request, create = False):
        carrito = None
        if 'carrito' in request.session:
            carrito_id = request.session['carrito']
            try:
                carrito = Carrito.objects.get(id = carrito_id)
                if carrito.checkout:
                    del request.session['carrito']
                    carrito = None
            except Carrito.DoesNotExist:
                del request.session['carrito']

        if carrito is None:
            if create:
                carrito = Carrito()
                carrito.save()
                request.session['carrito'] = carrito.id
            else:
                raise Carrito.DoesNotExist

        return carrito

class Carrito(models.Model):
    checkout = models.BooleanField(default = False)
    objects = CarritoManager()
    fecha_creacion = models.DateTimeField(auto_now_add = True)
    fecha_checkout = models.DateTimeField(blank = True, null = True)

    def __iter__(self):
        return self.carritoitem_set.all()

    def __len__(self):
        return self.carritoitem_set.count()

    def items(self):
        return self.carritoitem_set.all()

    def total_diferentes_items(self):
        return len(self.items())
    
    def total_items(self):
        return sum([x.cantidad for x in self.items()])

    def tiene_producto(self, producto):
        return producto in [x.producto for x in self.items()]

    def agregar(self, producto, cantidad = 1):
        items = self.carritoitem_set.filter(producto = producto)
        if items:
            item = items[0]
            item.cantidad += cantidad
        else: 
            item = CarritoItem(carrito = self, producto = producto, cantidad = cantidad)

        item.save()

    def borrar(self, item_id):
        item = self.carritoitem_set.get(id=item_id)
        item.delete()

    def total_precio(self):
        return sum([x.precio_total for x in self.items()])

    def actualizar_item_cantidad(self, item_id, cantidad_str):
        item = self.carritoitem_set.get(id=item_id)
        cantidad = int(cantidad_str)
        if item.cantidad != cantidad:
            item.cantidad = cantidad
            item.save()

    def _set_unit_prices(self):
        for item in self.items():
            item.precio_checkout = item.producto.precio
            item.save()

    def hacer_pedido(self):
        self._set_unit_prices()
        self.fecha_checkout = datetime.datetime.now()
        self.checkout = True

class CarritoItem(models.Model):
    carrito = models.ForeignKey(Carrito)
    producto = models.ForeignKey(Producto)
    cantidad = models.IntegerField()
    fecha_creacion = models.DateTimeField(auto_now_add = True)
    precio_checkout = models.DecimalField(max_digits = 8, decimal_places = 2, blank = True, null = True)

    def __unicode__(self):
        return self.producto.descripcion

    @property
    def precio(self):
        if self.carrito.checkout:
            return self.precio_checkout
        
        return self.producto.precio

    @property
    def precio_total(self):
        return self.precio * self.cantidad
