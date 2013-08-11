from django.template.response import TemplateResponse
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from .models import Producto

def index(request, categoria = None, sub_categoria = None):
    productos = Producto.producto.all()
    titulo = "Todos"
    breadcrumb = [('Home', '/')]
    if categoria:
        productos = productos.filter(categoria__slug = categoria)
        if productos:
            titulo = productos[0].categoria.nombre
            categoria_url = reverse('productos.views.index', args=(categoria,))
            breadcrumb.append((titulo, categoria_url))

        if sub_categoria:
            productos = productos.filter(sub_categoria__slug = sub_categoria)
            if productos:
                sub_categoria_url = reverse('productos.views.index', args=(categoria, sub_categoria))
                breadcrumb.append((productos[0].sub_categoria.nombre, sub_categoria_url))


    return TemplateResponse(request, 'productos/index.html', { 'productos' : productos, 'titulo': titulo, 'breadcrumb': breadcrumb } )

def detalle(request, producto):
    producto = get_object_or_404(Producto, slug = producto)
    relacionados = producto.categoria.producto_set.all()[:5]

    breadcrumb = [('Home', '/')]
    categoria_url = reverse('productos.views.index', args=(producto.categoria.slug,))
    breadcrumb.append((producto.categoria.nombre, categoria_url))
    if producto.sub_categoria:
        sub_categoria_url = reverse('productos.views.index', args=(producto.categoria.slug, producto.sub_categoria.slug))
        breadcrumb.append((producto.sub_categoria.nombre, sub_categoria_url))

    producto_url = reverse('productos.views.detalle', args=(producto.slug,))
    breadcrumb.append((producto.titulo, producto_url))

    return TemplateResponse(request, 'productos/detalle.html', { 'producto' : producto, 'relacionados':relacionados,'breadcrumb': breadcrumb } )
