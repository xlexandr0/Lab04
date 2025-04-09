from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_actividades, name='lista_actividades'),
    path('agregar/', views.agregar_actividad, name='agregar_actividad'),
    path('editar/<int:pk>/', views.editar_actividad, name='editar_actividad'),
    path('eliminar/<int:pk>/', views.eliminar_actividad, name='eliminar_actividad'),
]
