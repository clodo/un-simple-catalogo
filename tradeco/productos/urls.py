from django.conf.urls.defaults import url, patterns, include

urlpatterns = patterns('productos.views',
    url(r'^producto/(?P<producto>[a-z0-9\-]+)?$', 'detalle'),
    url(r'^(?P<categoria>[a-z0-9\-]+)?/(?P<sub_categoria>[a-z0-9\-]+)?$', 'index'),
    url(r'^(?P<categoria>[a-z0-9\-]+)?$', 'index'),
)

#urlpatterns += patterns('', 
#   url(r'^login/$', 'django.contrib.auth.views.login'),
#)
