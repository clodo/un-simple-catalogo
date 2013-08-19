from django.conf.urls.defaults import url, patterns, include

urlpatterns = patterns('productos.views',
    url(r'^producto/(?P<producto>[a-z0-9\-]+)?$', 'detalle'),
    url(r'^(?P<categoria>\w+)?/(?P<sub_categoria>\w+)?$', 'index'),
    url(r'^(?P<categoria>\w+)?$', 'index'),
)

#urlpatterns += patterns('', 
#   url(r'^login/$', 'django.contrib.auth.views.login'),
#)
