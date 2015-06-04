from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'circulacion.views.home', name='home'),
    url(r'^login/$', 'circulacion.views.login',name='login'),
    url(r'^clientes/$', 'circulacion.views.set_clientes',name='clientes'),
    url(r'^cierre/$', 'circulacion.views.set_cierre',name='cierre'),
    url(r'^tiraje/agregar$', 'circulacion.views.set_tiraje',name='tiraje'),
    url(r'^tiraje/modificar$', 'circulacion.views.upt_tiraje',name='tiraje2'),
    url(r'^guia/modificar$', 'circulacion.views.upd_guia',name='guia2'),
    url(r'^guia/agregar$', 'circulacion.views.set_guia',name='guia'),
    #url(r'^empleados/$', 'circulacion.views.set_empleados',name='set_empleados'),
    url(r'^suscripciones/$', 'circulacion.views.set_suscripcion',name='set_suscripcion'),
    url(r'^plan/$', 'circulacion.views.set_planes', name='set_planes'),
    url(r'^control/$', 'circulacion.views.set_control', name='set_control'),
    url(r'^asesor/$', 'circulacion.views.set_asesores', name='set_asesores'),
    url(r'^plan/modificar$', 'circulacion.views.upt_plan', name='plan_modificar'),
    url(r'^admin/', include(admin.site.urls)),
)
