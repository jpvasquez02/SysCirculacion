from django import forms
from django.forms import ModelForm
from circulacion.models import *

class planesForm(forms.ModelForm):
    class Meta:
        model = planes
        fields='__all__'

class asesoresForm(forms.ModelForm):
    class Meta:
        model = asesores
        fields='__all__'

class controlForm(forms.ModelForm):
    class Meta:
        model = control
        fields='__all__'
    
    