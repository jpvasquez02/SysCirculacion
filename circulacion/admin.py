from django.contrib import admin
from circulacion.models import *

class PlanesAdmin(admin.ModelAdmin):
	List_display = ('CodigoPlan','Nombre','Precio')

class SupervisoresAdmin(admin.ModelAdmin):
	pass

class RutasAdmin(admin.ModelAdmin):
	pass

class AsesoresAdmin(admin.ModelAdmin):
	pass

class RepartidoresAdmin(admin.ModelAdmin):
	ordering=['NombreRepartidor']
	List_display=('NombreRepartidor','Telefono')

class DeptoAdmin(admin.ModelAdmin):
	pass	

class CiudadAdmin(admin.ModelAdmin):
	pass

class ControlAdmin(admin.ModelAdmin):
	pass

class ClientesAdmin(admin.ModelAdmin):
	ordering=['Codigo']

class SuscripcionesAdmin(admin.ModelAdmin):
	ordering=['Codigo']
	List_display=('Codigo','Suscriptor','Ruta')

class EmpleadosAdmin(admin.ModelAdmin):
	pass

admin.site.register(asesores,AsesoresAdmin)
admin.site.register(departamentos,DeptoAdmin)
admin.site.register(empleados,EmpleadosAdmin)
admin.site.register(ciudades,CiudadAdmin)
admin.site.register(clientes,ClientesAdmin)
admin.site.register(control,ControlAdmin)
admin.site.register(planes,PlanesAdmin)
admin.site.register(repartidores,RepartidoresAdmin)
admin.site.register(rutas,RutasAdmin)
admin.site.register(suscripcion)
admin.site.register(supervisores,SupervisoresAdmin)