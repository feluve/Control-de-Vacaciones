from django.urls import path
from .views import nuevo_usuario, guardar_nuevo_usuario, olvide_contrasena, link_expirado, link_recuperacion, contrasena_nueva, cambiar_contrasena

from django.conf import settings

urlpatterns = [
    path("nuevo_usuario/", nuevo_usuario, name="nuevo_usuario"),
    path("guardar_nuevo_usuario/", guardar_nuevo_usuario,
         name="guardar_nuevo_usuario"),
    
    path("olvide_contrasena", olvide_contrasena),
    path("link_expirado", link_expirado),
    path("link_recuperacion/<str:usuario>", link_recuperacion),
    path("contrasena_nueva/<str:usuario>/<str:token>", contrasena_nueva),
    path("cambiar_contrasena/<str:usuario>/<str:token>/<str:contrasena>",
         cambiar_contrasena),
]