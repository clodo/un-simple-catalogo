from django.conf.urls import patterns, include, url

urlpatterns = patterns('carritos.views',
    url(r'hacer-pedido', 'checkout'),
    url(r'agregar$', 'agregar_producto'),
    url(r'borrar$', 'borrar_item'),
    url(r'actualizar$', 'actualizar_cantidad'),
    url(r'^$', 'carrito'),
)

