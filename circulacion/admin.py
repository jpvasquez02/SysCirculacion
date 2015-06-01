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
	pass

class DeptoAdmin(admin.ModelAdmin):
	pass	

class CiudadAdmin(admin.ModelAdmin):
	pass

class ControlAdmin(admin.ModelAdmin):
	pass

admin.site.register(asesores,AsesoresAdmin)
admin.site.register(departamentos,DeptoAdmin)
admin.site.register(ciudades,CiudadAdmin)
admin.site.register(control,ControlAdmin)
admin.site.register(planes,PlanesAdmin)
admin.site.register(repartidores,RepartidoresAdmin)
admin.site.register(rutas,RutasAdmin)
admin.site.register(supervisores,SupervisoresAdmin)