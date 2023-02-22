from django.contrib import admin
from django.contrib.auth.models import User
from vacaciones.models import Solicitud_Vacaciones, Perfil, Dias_Festivos_Oficiales

# Register your models here.

# admin.site.register(Solicitud_Vacaciones)
# admin.site.register(Perfil)
# admin.site.register(Dias_Festivos_Oficiales)


@admin.register(Solicitud_Vacaciones)
class AdminSolicitudVaciones(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'nombre', 'dias', 'fecha',
                    'fecha_inicio', 'fecha_fin', 'jefe', 'estado')
    # ordering = ('fecha',)
    search_fields = ('nombre', 'jefe', 'estado')
    list_editable = ('dias', 'jefe', 'estado')
    # list_display_links = ('nombre',)
    # list_filter = ('nombre',)
    list_per_page = 20
    # exclude = ('dias',)


@admin.register(Perfil)
class AdminPerfil(admin.ModelAdmin):
    list_display = ('usuario', 'fecha_ingreso', 'vigencia_dias_vacaciones', 'area',
                    'dias_vacaciones_disp', 'jefe', 'rol')
    ordering = ('id',)
    search_fields = ('nombre', 'usuario', 'fecha_ingreso', 'jefe', 'rol')
    list_editable = ('fecha_ingreso', 'vigencia_dias_vacaciones', 'area',
                     'dias_vacaciones_disp', 'jefe', 'rol')
    # list_display_links = ('usuario',)
    list_filter = ('usuario', 'jefe', 'rol', 'area')
    list_per_page = 20
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
