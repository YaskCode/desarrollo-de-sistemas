"""Interacción mínima: registrar y consultar exclusivamente las propias."""
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods
from gestion.forms import PostulacionForm
from gestion.models import Postulacion
from gestion.services import registrar_postulacion


@login_required
@require_http_methods(["GET", "POST"])
def inicio(request):
    form = PostulacionForm(request.POST if request.method == "POST" else None)
    status = 200
    if request.method == "POST":
        if form.is_valid():
            _, creada = registrar_postulacion(
                estudiante=request.user, oferta=form.cleaned_data["oferta"],
            )
            if creada:
                messages.success(request, "Postulación registrada. No implica aprobación académica.")
                return redirect("inicio")
            form.add_error(None, "Ya existe una postulación tuya a esta oferta.")
            status = 409
        else:
            status = 400
    postulaciones = Postulacion.objects.filter(estudiante=request.user).select_related("oferta")
    return render(request, "gestion/inicio.html", {
        "form": form, "postulaciones": postulaciones,
    }, status=status)
