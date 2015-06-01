from django.db import models
from django.contrib.auth.models import User

class planes(models.Model):
	CodigoPlan=models.CharField(max_length=4)
	Nombre=models.CharField(max_length=50)
	Precio=models.DecimalField(max_digits=7,decimal_places=2)

	class Meta:
		ordering=['CodigoPlan','Nombre','Precio']
		verbose_name_plural='Planes'

	def __str__(self):
		return self.CodigoPlan

class supervisores(models.Model):
	Codigo=models.IntegerField(max_length=10, primary_key=True)
	Nombre=models.CharField(max_length=140)

	class Meta:
		verbose_name_plural='Supervisores'

	def __str__(self):
		return '%s - %s' % (self.Codigo,self.Nombre)

class rutas(models.Model):
	NombreRuta=models.CharField(max_length=35)
	Colonias=models.TextField()

	class Meta:
		ordering=['NombreRuta']
		verbose_name_plural='Rutas'

	def __str__(self):
		return self.NombreRuta

class asesores(models.Model):
	NombreAsesor=models.CharField(max_length=140)

	class Meta:
		ordering=['NombreAsesor']
		verbose_name_plural='Asesores'

	def __str__(self):
		return self.NombreAsesor

class repartidores(models.Model):
	NombreRepartidor=models.CharField(max_length=140)
	Telefono=models.CharField(max_length=10)

	class Meta:
		ordering=['NombreRepartidor']
		verbose_name_plural='Repartidores'

	def __str__(self):
		return self.NombreRepartidor

class departamentos(models.Model):
	Departamento=models.CharField(max_length=140)

	class Meta:
		verbose_name_plural='Departamentos'

	def __str__(self):
		return self.Departamento

class ciudades(models.Model):
	Departamento=models.ForeignKey(departamentos)
	Municipio=models.CharField(max_length=140)

	class Meta:
		ordering=['Departamento']
		verbose_name_plural='Ciudades'

	def __str__(self):
		return self.Municipio

class control(models.Model):
	Opciones= (
		(1,'Faltaron X Vendedores'),
		(2,'Semaforo en mal Estado'),
		(3,'Falta de Energía Eléctrica'),
		(4,'Calle Cerrada'),
		(5,'Manifestacion'),
		)
	Fecha=models.DateField()
	Supervisor=models.ForeignKey(supervisores)
	Motivo=models.CharField(max_length=140,choices=Opciones)
	Comentarios=models.TextField(blank=True,null=True)

	class Meta:
		ordering=['Fecha']
		verbose_name_plural='Hoja de Control'

	def __str__(self):
		return '%s - %s' % (self.Fecha,self.Motivo)
