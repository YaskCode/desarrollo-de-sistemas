import pytest
from django.contrib.auth import get_user_model
from django.db import IntegrityError, connection, transaction


@pytest.mark.django_db
def test_escritura_en_postgresql():
    assert connection.vendor == "postgresql"
    user = get_user_model().objects.create_user(username="estudiante_prueba")
    assert get_user_model().objects.filter(pk=user.pk).exists()


@pytest.mark.django_db
def test_integridad_de_usuario():
    User = get_user_model()
    User.objects.create_user(username="estudiante_prueba")
    with pytest.raises(IntegrityError):
        with transaction.atomic():
            User.objects.create_user(username="estudiante_prueba")
    assert User.objects.filter(username="estudiante_prueba").count() == 1


def test_administracion_requiere_inicio_de_sesion(client):
    response = client.get("/admin/")
    assert response.status_code == 302
    assert "/admin/login/" in response["Location"]
