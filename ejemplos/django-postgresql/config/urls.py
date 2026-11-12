"""Rutas del ejemplo."""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from gestion.views import inicio

urlpatterns = [
    path("admin/", admin.site.urls),
    path("entrar/", auth_views.LoginView.as_view(template_name="gestion/login.html"), name="login"),
    path("salir/", auth_views.LogoutView.as_view(), name="logout"),
    path("", inicio, name="inicio"),
]
