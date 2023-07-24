from django.urls import path
from .views import asistenciaQR, registroAsistenciaQR, dispositivo, registroDispositivo

urlpatterns = [
    path('asistenciaQR/', asistenciaQR, name='asistenciaQR'),
    path('registroAsistenciaQR/<str:fecha_hora>', registroAsistenciaQR, name='registroAsistenciaQR'),
    path('dispositivo/', dispositivo, name='dispositivo'),
    path('registroDispositivo/<str:pantalla>/<str:plataforma>/<str:nucleos>/', registroDispositivo, name='registroDispositivo'),
]

