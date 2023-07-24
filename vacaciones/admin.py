from django.contrib import admin
from django.contrib.auth.models import User
from vacaciones.models import Solicitud_Vacaciones, Perfil, Dias_Festivos_Oficiales

from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

# admin.site.register(Solicitud_Vacaciones)
# admin.site.register(Perfil)
# admin.site.register(Dias_Festivos_Oficiales)
# admin.site.register(Jefes)

# @admin.register(Jefes())
# class AdminJefes(admin.ModelAdmin):
# list_display = ('nombre',)
# ordering = ('nombre',)
# search_fields = ('nombre',)
# list_editable = ('nombre', )
# list_display_links = ('nombre',)
# list_filter = ('nombre',)
# list_per_page = 20
# exclude = ('nombre',)


@admin.register(Solicitud_Vacaciones)
class AdminSolicitudVaciones(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'nombre', 'dias', 'fecha',
                    'fecha_inicio', 'fecha_fin', 'jefe', 'estado', 'comentario_solicitud', 'comentario_jefe')
    ordering = ('-id',)
    search_fields = ('nombre', 'jefe', 'estado')
    list_editable = ('dias', 'jefe', 'estado')
    # list_display_links = ('nombre',)
    list_filter = ('estado',)
    list_per_page = 20
    # exclude = ('dias',)


@admin.register(Perfil)
class AdminPerfil(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('usuario', 'fecha_ingreso', 'dias_vacaciones_disp',
                    'vigencia_dias_vacaciones', 'jefe', 'area', 'fecha_nacimiento', 'rol', 'id_asistencia')
    ordering = ('usuario',)
    search_fields = ('usuario',)
    list_editable = ('fecha_ingreso', 'vigencia_dias_vacaciones', 'jefe', 'area',
                     'dias_vacaciones_disp', 'fecha_nacimiento', 'rol', 'id_asistencia')
    list_display_links = ('usuario',)
    list_filter = ('jefe', 'rol', 'area')
    list_per_page = 50
    # exclude = ('dias',)


@admin.register(Dias_Festivos_Oficiales)
class AdminDiasFestivosOficiales(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'dia_festivo')
    ordering = ('dia_festivo',)
    search_fields = ('nombre',)
    list_editable = ('nombre', 'dia_festivo', )
    # list_display_links = ('nombre',)
    # list_filter = ('nombre',)
    list_per_page = 20
    # exclude = ('dias',)
