from django.conf.urls.defaults import url, patterns, include

urlpatterns = patterns('productos.views',
    url(r'^(?P<categoria>\w+)?/(?P<sub_categoria>\w+)?$', 'productos'),
    url(r'^(?P<categoria>\w+)?$', 'productos'),
)

#urlpatterns += patterns('', 
#   url(r'^login/$', 'django.contrib.auth.views.login'),
#)
