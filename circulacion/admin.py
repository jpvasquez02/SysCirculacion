from django.contrib import admin
from circulacion.models import *

class PlanesAdmin(admin.ModelAdmin):
	List_display = ('CodigoPlan','Nombre','Precio')

admin.site.register(planes,PlanesAdmin)