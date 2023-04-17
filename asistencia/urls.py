from django.urls import path

from asistencia.views import carga_asistencia_excel, asistencia

urlpatterns = [

    path('carga_asistencia_excel/', carga_asistencia_excel,
         name='carga_asistencia_excel'),
    path('asistencia/', asistencia, name='asistencia')

]
