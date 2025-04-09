from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import get_template
from .models import Actividad
from .forms import ActividadForm
from xhtml2pdf import pisa

def lista_actividades(request):
    actividades = Actividad.objects.all()
    return render(request, 'actividades/lista_actividades.html', {'actividades': actividades})

def agregar_actividad(request):
    if request.method == 'POST':
        form = ActividadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_actividades')
    else:
        form = ActividadForm()
    return render(request, 'actividades/agregar_actividad.html', {'form': form})

def editar_actividad(request, id):
    actividad = Actividad.objects.get(id=id)
    if request.method == 'POST':
        form = ActividadForm(request.POST, instance=actividad)
        if form.is_valid():
            form.save()
            return redirect('lista_actividades')
    else:
        form = ActividadForm(instance=actividad)
    return render(request, 'actividades/editar_actividad.html', {'form': form, 'actividad': actividad})

def generar_carta_poder(request, actividad_id):
    actividad = Actividad.objects.get(id=actividad_id)
    context = {
        'nombre_actividad': actividad.nombre,
        'descripcion': actividad.descripcion,
        'fecha': actividad.fecha,
        'hora_inicio': actividad.hora_inicio,
        'hora_fin': actividad.hora_fin,
        'aula': actividad.aula,
    }
    template = get_template('actividades/carta_poder.html')
    html = template.render(context)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="carta_poder.pdf"'
    pisa.CreatePDF(html, dest=response)
    return response
