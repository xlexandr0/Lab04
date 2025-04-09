from django.shortcuts import render, redirect
from .models import Actividad
from .forms import ActividadForm
from django.http import HttpResponseRedirect
from django.urls import reverse

def lista_actividades(request):
    actividades = Actividad.objects.all()
    return render(request, 'actividades/lista_actividades.html', {'actividades': actividades})

def agregar_actividad(request):
    if request.method == 'POST':
        form = ActividadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_actividades')  # Redirigir a la lista de actividades
    else:
        form = ActividadForm()
    return render(request, 'actividades/agregar_actividad.html', {'form': form})

def editar_actividad(request, pk):
    actividad = Actividad.objects.get(pk=pk)
    if request.method == 'POST':
        form = ActividadForm(request.POST, instance=actividad)
        if form.is_valid():
            form.save()
            return redirect('lista_actividades')  # Redirigir a la lista de actividades
    else:
        form = ActividadForm(instance=actividad)
    return render(request, 'actividades/editar_actividad.html', {'form': form})

def eliminar_actividad(request, pk):
    actividad = Actividad.objects.get(pk=pk)
    actividad.delete()
    return HttpResponseRedirect(reverse('lista_actividades'))