"""Datos sintéticos de demostración; contraseña suministrada en la sesión."""
import os
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError
from gestion.models import Oferta


class Command(BaseCommand):
    help = "Prepara dos cuentas sin privilegios y una oferta de demostración."

    def handle(self, *args, **options):
        password = os.environ.get("PP4_DEMO_PASSWORD", "")
        if len(password) < 12:
            raise CommandError("Definir PP4_DEMO_PASSWORD con al menos 12 caracteres para la demostración local.")
        User = get_user_model()
        for username in ("estudiante_uno", "estudiante_dos"):
            user, creada = User.objects.get_or_create(username=username)
            if creada:
                user.set_password(password)
                user.save()
        Oferta.objects.get_or_create(titulo="Oferta sintética de pasantía")
        self.stdout.write("Datos disponibles: estudiante_uno, estudiante_dos y oferta sintética. No se cambian contraseñas existentes.")
