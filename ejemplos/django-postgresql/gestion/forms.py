"""La identidad se obtiene de la sesión, nunca del formulario."""
from django import forms
from gestion.models import Oferta


class PostulacionForm(forms.Form):
    oferta = forms.ModelChoiceField(queryset=Oferta.objects.none(), label="Oferta")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["oferta"].queryset = Oferta.objects.filter(activa=True).order_by("pk")
