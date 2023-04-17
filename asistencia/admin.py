from django.contrib import admin
from asistencia.models import Asistencia


# Register your models here.
@admin.register(Asistencia)
class Asistencia(admin.ModelAdmin):
    list_display = ('idUsuario', 'nombre', 'fecha_hora')
    # list_editable = ('fecha_hora',)
    ordering = ('-fecha_hora',)
    search_fields = ('idUsuario', 'nombre')
    list_per_page = 100
