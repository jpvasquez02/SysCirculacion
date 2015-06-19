from django.shortcuts import render, render_to_response, get_object_or_404
from django.template.context import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import condition
import json
from circulacion.models import *
from circulacion.forms import *

@login_required
def home(request):
	template="index.html"
	return render_to_response(template)

def login(request):
	template='login.html'
	return render_to_response(template)

@login_required
def set_planes(request):
	if request.method=='POST':
		form=planesForm(request.POST)

		if form.is_valid():
			plan=planes()

			plan.CodigoPlan=request.POST.get("CodigoPlan","")
			plan.Nombre=request.POST.get("Nombre","")
			plan.Precio=request.POST.get("Precio","")

			plan.save()

			return HttpResponseRedirect('/plan/')

	else:
		form = planesForm()

	return render (request, 'plan.html', {'form': form})

@login_required
def set_asesores(request):
	if request.method=='POST':
		form=asesoresForm(request.POST)

		if form.is_valid():
			asesor = asesores()

			asesor.NombreAsesor=request.POST.get("NombreAsesor","")

			asesor.save()

			return HttpResponseRedirect('/asesor/')

	else:
		form= asesoresForm()

	return render(request, 'asesores.html', {'form':form})

@login_required
def set_control(request):
	if request.method=='POST':
		form=controlForm(request.POST)

		if form.is_valid():
			crt = control()

			crt.Fecha=request.POST.get("Fecha","")
			crt.Supervisor=control.objects.get(pk=request.POST.get("Nombre",""))
			crt.Motivo=request.POST.get("Motivo","")
			crt.Comentarios=request.POST.get("Comentarios","")

			crt.save()

			return HttpResponseRedirect('/control/')

	else:
		form= controlForm()

	return render(request, 'control.html', {'form':form})	

@login_required
def set_clientes(request):
	if request.method=='POST':
		form=clientesForm(request.POST)

		if form.is_valid():

			emp=clientes()

			emp.Codigo=request.POST.get("Codigo","")
			emp.TipoCliente=request.POST.get("TipoCliente","")
			emp.Nombre=request.POST.get("Nombre","")
			emp.Identificacion=request.POST.get("Identificacion","")
			emp.FechaNacimiento=request.POST.get("FechaNacimiento","")
			emp.Genero=request.POST.get("Genero","")
			emp.Telefono=request.POST.get("Telefono","")
			emp.Celular=request.POST.get("Celular","")
			emp.Departamento=departamentos.objects.get(pk=request.POST.get("Departamento",""))
			emp.Ciudad=ciudades.objects.get(pk=request.POST.get("Ciudad",""))
			emp.Colonia=request.POST.get("Colonia","")
			emp.Calle=request.POST.get("Calle","")
			emp.Avenida=request.POST.get("Avenida","")
			emp.Referencia=request.POST.get("Referencia","")
			emp.Correo=request.POST.get("Correo","")
			emp.latitud=request.POST.get("latitud","")
			emp.longitud=request.POST.get("longitud","")

			emp.save()

			return HttpResponseRedirect('/clientes/')

	else:
		form=clientesForm()

	return render(request, 'NewClient.html', {'form':form})

@login_required
def set_suscripcion(request):
	if request.method=='POST':
		form=suscripcionForm(request.POST)

		if form.is_valid():

			s=suscripcion()

			s.Codigo=request.POST.get("Codigo","")
			s.Suscriptor=clientes.objects.get(pk=request.POST.get("Suscriptor",""))
			s.Categoria=request.POST.get("Categoria","")
			s.Cantidad=request.POST.get("Cantidad","")
			s.Plan=planes.objects.get(pk=request.POST.get("Plan",""))
			s.Descuento=request.POST.get("Descuento","")
			s.Valor=request.POST.get("Valor","")
			s.Contrato=request.POST.get("Contrato","")
			s.Recibo=request.POST.get("Recibo","")
			s.Asesor=asesores.objects.get(pk=request.POST.get("Asesor",""))
			s.Ruta=rutas.objects.get(pk=request.POST.get("Ruta",""))
			s.Entrega=request.POST.get("Entrega","")
			s.Comentarios=request.POST.get("Comentarios","")
			s.Tipo=request.POST.get("Tipo","")
			s.Inicio=request.POST.get("Inicio","")
			s.Fin=request.POST.get("Fin","")
			s.Repartidor=repartidores.objects.get(pk=request.POST.get("Repartidor",""))

		
			s.save()

			return HttpResponseRedirect('/suscripciones/')
			
	else:
		form=suscripcionForm
		
	return render(request, 'suscripciones.html', {'form':form})


@login_required
def set_cierre(request):
	c=suscripcion.objects.all()
	template='cierre.html'
	if request.method=='POST':
		s=suscripcion.objects.filter(Codigo=request.POST.get("Codigo","")).update(Suscriptor=request.POST.get("Suscriptor",""))

	return render(request,template,locals(),context_instance=RequestContext(request))

@login_required
def upt_tiraje(request):
	t=tiraje.objects.all()
	template='tiraje.html'
	if request.method=='POST':
		tr=tiraje.objects.filter(pk=request.POST.get("id","")).update(Lunes=request.POST.get("Lunes",""))

	return render(request,template,locals(),context_instance=RequestContext(request))

@login_required
def set_guia(request):
	if request.method=='POST':
		form=guiaForm(request.POST)

		if form.is_valid():

			form.save()

			return HttpResponseRedirect('/guia/agregar')

	else:
		form=guiaForm()

	return render (request, 'addguia.html', {'form':form})

@login_required
def upd_guia(request):
	s=suscripcion.objects.all()
	template='guia.html'
	if request.method=='POST':
		g=guia.objects.filter(pk=request.POST.get("id","")).update(Ruta=request.POST.get("Ruta",""))

	return render(request,template,locals(),context_instance=RequestContext(request))

@login_required
def set_tiraje(request):
	if request.method=='POST':
		form=tirajeForm(request.POST)


		if form.is_valid():

			form.save()

			return HttpResponseRedirect('/tiraje/agregar')

	else:
		form=tirajeForm()

	return render (request, 'tiraje_agregar.html', {'form':form})

@login_required
def upt_plan(request):
	qr=planes.objects.all()
	template='plan_mod.html'
	if request.method=='POST':
		p=planes.objects.filter(pk=request.POST.get("id","")).update(CodigoPlan=request.POST.get("codigo",""))
		p2=planes.objects.filter(pk=request.POST.get("id","")).update(Nombre=request.POST.get("nombre",""))
		p3=planes.objects.filter(pk=request.POST.get("id","")).update(Precio=request.POST.get("precio",""))

	return render(request, template,locals(),context_instance=RequestContext(request))












