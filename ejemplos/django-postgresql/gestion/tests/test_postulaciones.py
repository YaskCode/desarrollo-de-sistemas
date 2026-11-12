"""Pruebas de reglas, persistencia y aislamiento de cuentas."""
import pytest
from django.contrib.auth import get_user_model
from django.db import IntegrityError, connection, transaction
from django.test import Client
from gestion.models import Oferta, Postulacion
from gestion.services import registrar_postulacion


@pytest.fixture
def datos(db):
    User = get_user_model()
    return (
        User.objects.create_user(username="estudiante_uno"),
        User.objects.create_user(username="estudiante_dos"),
        Oferta.objects.create(titulo="Oferta sintética"),
    )


def test_usa_postgresql():
    assert connection.vendor == "postgresql"


def test_anonimo_no_puede_consultar(client):
    response = client.get("/")
    assert response.status_code == 302
    assert response["Location"].startswith("/entrar/")


def test_anonimo_no_puede_registrar(client):
    assert client.post("/", {"oferta": 1}).status_code == 302


def test_primera_postulacion(datos):
    uno, _, oferta = datos
    p, creada = registrar_postulacion(estudiante=uno, oferta=oferta)
    assert creada
    assert p.estudiante == uno
    assert Postulacion.objects.count() == 1


def test_segundo_intento_no_duplica(datos):
    uno, _, oferta = datos
    original, _ = registrar_postulacion(estudiante=uno, oferta=oferta)
    repetida, creada = registrar_postulacion(estudiante=uno, oferta=oferta)
    assert not creada
    assert repetida.pk == original.pk
    assert Postulacion.objects.count() == 1


def test_bd_rechaza_duplicado_aunque_se_omita_servicio(datos):
    uno, _, oferta = datos
    Postulacion.objects.create(estudiante=uno, oferta=oferta)
    with pytest.raises(IntegrityError):
        with transaction.atomic():
            Postulacion.objects.create(estudiante=uno, oferta=oferta)
    assert Postulacion.objects.count() == 1


def test_otro_estudiante_puede_postular_a_misma_oferta(datos):
    uno, dos, oferta = datos
    registrar_postulacion(estudiante=uno, oferta=oferta)
    _, creada = registrar_postulacion(estudiante=dos, oferta=oferta)
    assert creada
    assert Postulacion.objects.count() == 2


def test_mismo_estudiante_puede_postular_a_otra_oferta(datos):
    uno, _, oferta = datos
    otra = Oferta.objects.create(titulo="Otra oferta")
    registrar_postulacion(estudiante=uno, oferta=oferta)
    _, creada = registrar_postulacion(estudiante=uno, oferta=otra)
    assert creada
    assert Postulacion.objects.count() == 2


def test_post_correcto_redirige_y_muestra_confirmacion(client, datos):
    uno, _, oferta = datos
    client.force_login(uno)
    response = client.post("/", {"oferta": oferta.pk}, follow=True)
    assert response.redirect_chain == [("/", 302)]
    assert "No implica aprobación académica" in response.content.decode()
    assert Postulacion.objects.get().estudiante == uno


def test_post_duplicado_devuelve_conflicto_sin_segunda_fila(client, datos):
    uno, _, oferta = datos
    client.force_login(uno)
    client.post("/", {"oferta": oferta.pk})
    response = client.post("/", {"oferta": oferta.pk})
    assert response.status_code == 409
    assert "Ya existe" in response.content.decode()
    assert Postulacion.objects.count() == 1


def test_oferta_inexistente_no_crea_postulacion(client, datos):
    uno, _, _ = datos
    client.force_login(uno)
    assert client.post("/", {"oferta": 999999}).status_code == 400
    assert not Postulacion.objects.exists()


def test_oferta_inactiva_no_se_puede_seleccionar(client, datos):
    uno, _, oferta = datos
    oferta.activa = False
    oferta.save()
    client.force_login(uno)
    assert client.post("/", {"oferta": oferta.pk}).status_code == 400
    assert not Postulacion.objects.exists()


def test_campo_estudiante_falsificado_no_cambia_identidad(client, datos):
    uno, dos, oferta = datos
    client.force_login(uno)
    assert client.post("/", {"oferta": oferta.pk, "estudiante": dos.pk}).status_code == 302
    assert Postulacion.objects.get().estudiante == uno


def test_cuenta_solo_consulta_sus_registros(client, datos):
    uno, dos, oferta = datos
    privada = Oferta.objects.create(titulo="Oferta exclusiva de otra cuenta")
    registrar_postulacion(estudiante=dos, oferta=privada)
    registrar_postulacion(estudiante=uno, oferta=oferta)
    client.force_login(uno)
    response = client.get("/")
    assert list(response.context["postulaciones"].values_list("estudiante_id", flat=True)) == [uno.pk]


def test_csrf_exigido_para_registrar(datos):
    uno, _, oferta = datos
    client = Client(enforce_csrf_checks=True)
    client.force_login(uno)
    assert client.post("/", {"oferta": oferta.pk}).status_code == 403
    assert not Postulacion.objects.exists()


def test_metodo_no_admitido(client, datos):
    uno, _, _ = datos
    client.force_login(uno)
    assert client.delete("/").status_code == 405
