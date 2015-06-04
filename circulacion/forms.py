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

class clientesForm(forms.ModelForm):
    class Meta:
        model = clientes
        fields='__all__'
        widgets = {
            'FechaNacimiento': forms.DateInput(attrs={'class': 'datepicker','type':'date','dateformat':'yy-mm-dd'})
    }
    
class suscripcionForm(forms.ModelForm):
    class Meta:
        model = suscripcion
        fields='__all__'
        widgets={
        'Inicio': forms.DateInput(attrs={'class': 'datepicker','type':'date'}),
        'Fin': forms.DateInput(attrs={'class': 'datepicker','type':'date'})
        }

class cierreForm(forms.ModelForm):
    class Meta:
        model = cierre
        fields='__all__'
        widgets={
        'FechaPago': forms.DateInput(attrs={'class': 'datepicker','type':'date'}),
        'Inicio': forms.DateInput(attrs={'class': 'datepicker','type':'date'}),
        'Fin': forms.DateInput(attrs={'class': 'datepicker','type':'date'})

        }

class guiaForm(forms.ModelForm):
    class Meta:
        model = guia
        fields='__all__'
        widgets={
        'Fecha': forms.DateInput(attrs={'class': 'datepicker','type':'date'})
        }

class tirajeForm(forms.ModelForm):
    class Meta:
        model = tiraje
        fields='__all__'
    
    
    