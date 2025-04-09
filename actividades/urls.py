from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_actividades, name='lista_actividades'),
    path('agregar/', views.agregar_actividad, name='agregar_actividad'),
]
