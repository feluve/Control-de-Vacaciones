from django.urls import path
from .views import vacaciones, registra_solicitud, aprobarSolicitud, rechazarSolicitud, vacaciones, notificarSolicitud, cancelarSolicitud

from django.conf import settings

app_name = "vacaciones"

urlpatterns = [
    path("", vacaciones, name="vacaciones"),

    path("registra_solicitud/<int:dias_solicitados>/<str:fecha_solicitud>/<str:fecha_final>/<str:comentario_solicitud>",
         registra_solicitud, name="registra_solicitud"),
    path("aprobarSolicitud/<int:id>/<str:comentario>", aprobarSolicitud),
    path("rechazarSolicitud/<int:id>/<str:comentario>", rechazarSolicitud),
    path("cancelarSolicitud/<int:id>/<str:comentario>", cancelarSolicitud),
    path("notificarSolicitud/<int:id>", notificarSolicitud),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
