from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_actividades, name='lista_actividades'),  # Página de listado de actividades
    path('agregar/', views.agregar_actividad, name='agregar_actividad'),  # Página para agregar actividad
    path('editar/<int:id>/', views.editar_actividad, name='editar_actividad'),  # Página para editar actividad
    path('carta_poder/<int:actividad_id>/', views.generar_carta_poder, name='carta_poder'),  # Generar carta poder
]
