"""Entidades y restricción de la regla hipotética RN-01."""
from django.conf import settings
from django.db import models


class Oferta(models.Model):
    titulo = models.CharField(max_length=150)
    activa = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo


class Postulacion(models.Model):
    estudiante = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    oferta = models.ForeignKey(Oferta, on_delete=models.PROTECT)
    creada = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [models.UniqueConstraint(
            fields=["estudiante", "oferta"], name="postulacion_unica_estudiante_oferta",
        )]
        ordering = ["-creada", "-pk"]
