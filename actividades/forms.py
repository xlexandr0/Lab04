from django import forms
from .models import Actividad

class ActividadForm(forms.ModelForm):
    class Meta:
        model = Actividad
        fields = ['nombre', 'descripcion', 'fecha', 'hora_inicio', 'hora_fin', 'profesor', 'aula']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'hora_inicio': forms.TimeInput(attrs={'type': 'time'}),
            'hora_fin': forms.TimeInput(attrs={'type': 'time'}),
        }
