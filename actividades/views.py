from django.shortcuts import render
from .models import Actividad

def lista_actividades(request):
    actividades = Actividad.objects.all()
    return render(request, 'actividades/lista_actividades.html', {'actividades': actividades})
