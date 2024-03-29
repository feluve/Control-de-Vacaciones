from django.contrib import admin
from django.urls import path, include
from vacaciones.views import salir
from usuarios.views import aviso

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include("vacaciones.urls")),
    path('', include("usuarios.urls")),
    path('', include("asistencia.urls")),

    path('', include("asistenciaQR.urls")),
    
    path('', include("encuesta.urls")),

    path("accounts/", include('django.contrib.auth.urls')),
    path("salir/", salir, name="salir"),
]
