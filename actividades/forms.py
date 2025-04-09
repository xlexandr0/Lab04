from django import forms
from .models import Actividad

class ActividadForm(forms.ModelForm):
    class Meta:
        model = Actividad
        fields = ['nombre', 'descripcion', 'fecha', 'hora_inicio', 'hora_fin', 'profesor', 'aula']
