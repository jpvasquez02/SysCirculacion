from django.shortcuts import render, render_to_response, get_object_or_404
from django.template.context import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
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
			emp.FechaNacimiento=request.POST.get("FechaNacimiento","")

			print (request.POST)

			emp.save()

	else:
		form=clientesForm()

	return render(request, 'NewClient.html', {'form':form})
	