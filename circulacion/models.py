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

class repartidores(models.Model):
	NombreRepartidor=models.CharField(max_length=140)
	Telefono=models.CharField(max_length=15,blank=True,null=True)

	class Meta:
		ordering=['NombreRepartidor']
		verbose_name_plural='Repartidores'

	def __str__(self):
		return self.NombreRepartidor


class clientes(models.Model):
	Codigo=models.IntegerField(max_length=10,primary_key=True)
	TipoCliente=models.CharField(max_length=50,choices=[('Empresarial','Empresarial'),('Residencial','Residencial')])
	Nombre=models.CharField(max_length=140)
	Identificacion=models.CharField(max_length=15)
	FechaNacimiento=models.DateField()
	Genero=models.CharField(max_length=15, blank=True,null=True, choices=[('F','Femenino'),('M','Masculino')])
	Telefono=models.IntegerField(max_length=15,blank=True,null=True)
	Celular=models.IntegerField(max_length=15,blank=True,null=True)
	Departamento=models.ForeignKey(departamentos)
	Ciudad=models.ForeignKey(ciudades)
	Colonia=models.CharField(max_length=140)
	Calle=models.CharField(max_length=30)
	Avenida=models.CharField(max_length=30)
	Referencia=models.CharField(max_length=140)
	Correo=models.EmailField()
	latitud=models.CharField(max_length=50)
	longitud=models.CharField(max_length=50)

	class Meta:
		ordering=['Nombre']
		verbose_name_plural='Clientes'

	def __str__(self):
		return '%s - %s' % (self.Codigo,self.Nombre)


class empleados(models.Model):
	Nombre=models.CharField(max_length=140)
	Puesto=models.CharField(max_length=140)

	class Meta:
		ordering=['Nombre']
		verbose_name_plural='Empleados'

	def __str__(self):
		return self.Nombre

class suscripcion(models.Model):
	Codigo=models.IntegerField(max_length=10,primary_key=True)
	Suscriptor=models.ForeignKey(clientes)
	Categoria=models.CharField(max_length=50,choices=[('Empresarial','Empresarial'),('Residencial','Residencial')])
	Cantidad=models.IntegerField(max_length=5)
	Plan=models.ForeignKey(planes)
	Descuento=models.DecimalField(max_digits=5,decimal_places=2,null=True,blank=True)
	Valor=models.DecimalField(max_digits=8,decimal_places=2)
	Contrato=models.IntegerField()
	Recibo=models.IntegerField()
	Asesor=models.ForeignKey(asesores)
	Ruta=models.ForeignKey(rutas)
	Entrega=models.CharField(max_length=5,choices=[('L-D','L-D'),('L-S','L-S'),('L-V','L-V')])
	Comentarios=models.TextField()
	Tipo=models.CharField(max_length=35,choices=[('Canje','Canje'),('Certificado','Certificado'),('Cortesia','Cortesia'),('DxP','Deducible Por Planilla'),('Pagado','Pagado')])
	Inicio=models.DateField()
	Fin=models.DateField()
	Repartidor=models.ForeignKey(repartidores)

	class Meta:
		ordering=['Codigo','Suscriptor']
		verbose_name_plural='Suscripciones'

	def __str__(self):
		return '%s - %s' % (self.Codigo,self.Suscriptor)

class tiraje(models.Model):
	Ruta=models.ForeignKey(rutas)
	Lunes=models.IntegerField(max_length=5)
	Martes=models.IntegerField(max_length=5)
	Miercoles=models.IntegerField(max_length=5)
	Jueves=models.IntegerField(max_length=5)
	Viernes=models.IntegerField(max_length=5)
	Sabado=models.IntegerField(max_length=5)
	Domingo=models.IntegerField(max_length=5)

	class Meta:
		ordering=['Ruta']
		verbose_name_plural='Tiraje'

	def __str__(self):
		return self.Ruta.NombreRuta

class cierre(models.Model):
	Vendedor=models.ForeignKey(empleados)
	Nombre=models.ForeignKey(suscripcion)
	Cantidad=models.IntegerField(max_length=5)
	Direccion=models.CharField(max_length=140)
	Tipo=models.ForeignKey(planes)
	Valor=models.DecimalField(max_digits=8,decimal_places=2)
	Recibo=models.CharField(max_length=10)
	ValorRecibido=models.DecimalField(max_digits=8,decimal_places=2)
	Comision=models.DecimalField(max_digits=8,decimal_places=2)
	FechaPago=models.DateField()
	Inicio=models.DateField()
	Fin=models.DateField()

	class Meta:
		verbose_name_plural='Cierre Circulación'

	def __str__(self):
		return '%s - %s' % (self.Vendedor.Nombre)

class recibo(models.Model):
	Codigo=models.AutoField(primary_key=True)
	Fecha=models.DateField()
	Nombre=models.ForeignKey(suscripcion)
	Plan=models.ForeignKey(planes)
	Tipo=models.CharField(max_length=35,choices=[('Canje','Canje'),('Certificado','Certificado'),('Cortesia','Cortesia'),('DxP','Deducible Por Planilla'),('Pagado','Pagado')])
	Descripcion=models.TextField()
	Valor=models.DecimalField(max_digits=8,decimal_places=2)

	class Meta:
		ordering=['Codigo','Fecha']
		verbose_name_plural='Recibos'

	def __str__(self):
		return '%s - %s - %s' % (self.Codigo,self.Fecha,self.suscripcion.Suscriptor)

class guia(models.Model):
	Fecha=models.DateField()
	Dia=models.CharField(max_length=10,choices=[('L','Lunes'),('M','Martes'),('K','Miercoles'),('J','Jueves'),('V','Viernes'),('S','Sabado'),('D','Domingo')])
	Ruta=models.ForeignKey(rutas)
	Supervisor=models.ForeignKey(supervisores,blank=True,null=True)
	Cliente=models.ForeignKey(suscripcion)
	Destino=models.CharField(max_length=140,blank=True,null=True)
	Envios=models.IntegerField(max_length=5,blank=True,null=True)
	Cortesias=models.IntegerField(max_length=5,blank=True,null=True)
	Suscripciones=models.IntegerField(max_length=5,blank=True,null=True)

	class Meta:
		ordering=['Ruta']
		verbose_name_plural='Guía de Producción'

	def __str__(self):
		return '%s - %s - %s' % (self.Fecha,self.Ruta.NombreRuta,self.suscripcion.Suscriptor)













