"""Administración local de los datos sintéticos."""
from django.contrib import admin
from gestion.models import Oferta, Postulacion
admin.site.register(Oferta)
admin.site.register(Postulacion)
