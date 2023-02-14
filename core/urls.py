from django.contrib import admin
from django.urls import path, include
from vacaciones.views import salir

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("vacaciones.urls")),

    path("accounts/", include('django.contrib.auth.urls')),
    path("salir/", salir, name="salir"),
]
