"""Registro idempotente respaldado por una restricción de BD."""
from gestion.models import Postulacion


def registrar_postulacion(*, estudiante, oferta):
    # La vista valida autorización y selección activa antes de invocar el servicio.
    # get_or_create se apoya en UNIQUE para resolver intentos del mismo par.
    return Postulacion.objects.get_or_create(estudiante=estudiante, oferta=oferta)
