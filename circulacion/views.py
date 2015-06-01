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
