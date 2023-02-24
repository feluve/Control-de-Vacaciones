from django.urls import path
from .views import vacaciones, registra_solicitud, aprobarSolicitud, rechazarSolicitud


from django.conf import settings

urlpatterns = [
    path("", vacaciones, name="vacaciones"),
    path("registra_solicitud/",
         registra_solicitud, name="registra_solicitud"),
    path("aprobarSolicitud/<int:id>/<str:comentario>", aprobarSolicitud),
    path("rechazarSolicitud/<int:id>/<str:comentario>", rechazarSolicitud),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
