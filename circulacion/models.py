from django.db import models
from django.contrib.auth.models import User

class planes(models.Model):
	CodigoPlan=models.CharField(max_length=4)
	Nombre=models.CharField(max_length=50)
	Precio=models.DecimalField(max_digits=7,decimal_places=2)

	class Meta:
		ordering=['CodigoPlan']
		verbose_name_plural='Planes'

	def __str__(self):
		return self.CodigoPlan
