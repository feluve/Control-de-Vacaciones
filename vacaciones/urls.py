from django.urls import path
from .views import vacaciones, registra_solicitud, aprobarSolicitud, rechazarSolicitud, olvide_contrasena, link_recuperacion, contrasena_nueva, cambiar_contrasena


from django.conf import settings

urlpatterns = [
    path("", vacaciones, name="vacaciones"),
    path("registra_solicitud/<int:dias_solicitados>/<str:fecha_solicitud>/<str:fecha_final>/<str:comentario_solicitud>",
         registra_solicitud, name="registra_solicitud"),
    path("aprobarSolicitud/<int:id>/<str:comentario>", aprobarSolicitud),
    path("rechazarSolicitud/<int:id>/<str:comentario>", rechazarSolicitud),

    path("olvide_contrasena", olvide_contrasena),
    path("link_recuperacion/<str:usuario>", link_recuperacion),
    path("contrasena_nueva/<str:usuario>/<str:token>", contrasena_nueva),
    path("cambiar_contrasena/<str:usuario>/<str:token>/<str:contrasena>",
         cambiar_contrasena),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
