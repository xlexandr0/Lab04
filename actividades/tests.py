from django.test import TestCase
from .models import Actividad

class ActividadTests(TestCase):
    def test_crear_actividad(self):
        actividad = Actividad.objects.create(
            nombre="Reunión de Padres",
            descripcion="Reunión informativa para padres de familia",
            fecha="2025-05-01",
            hora_inicio="10:00:00",
            hora_fin="12:00:00",
            profesor="Prof. Eustaquia",
            aula="Aula 1",
        )
        self.assertEqual(actividad.nombre, "Reunión de Padres")
