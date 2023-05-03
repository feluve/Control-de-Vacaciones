from django.contrib import admin
from .models import AsistenciaQR

from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

@admin.register(AsistenciaQR)
class AsistenciaQR(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'fecha_hora')
    ordering = ('usuario',)
    # search_fields = ('nombre', 'jefe', 'estado')
    # list_editable = ('dias', 'jefe', 'estado')
    # list_display_links = ('nombre',)
    # list_filter = ('nombre',)
    list_per_page = 20
    # exclude = ('dias',)

