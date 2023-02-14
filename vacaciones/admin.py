from django.contrib import admin
from django.contrib.auth.models import User
from vacaciones.models import Solicitud_Vacaciones, Perfil, Dias_Festivos_Oficiales

# Register your models here.

admin.site.register(Solicitud_Vacaciones)
# admin.site.register(Perfil)
# admin.site.register(Dias_Festivos_Oficiales)


# @admin.register(Solicitud_Vacaciones)
# class Admin(admin.ModelAdmin):
#     list_display = ('usuario', 'nombre', 'dias', 'fecha',
#                     'fecha_inicio', 'fecha_fin', 'jefe', 'estado')
#     ordering = ('fecha',)
#     search_fields = ('nombre', 'jefe', 'estado', 'fecha')
#     list_editable = ('usuario', 'dias', 'jefe', 'estado')
#     list_display_links = ('nombre',)
#     list_filter = ('nombre',)
#     list_per_page = 20
#     # exclude = ('dias',)


@admin.register(Perfil)
class Admin1(admin.ModelAdmin):
    list_display = ('usuario', 'fecha_ingreso', 'area',
                    'dias_vacaciones_disp', 'vigencia_dias_vacaciones_disp', 'jefe', 'rol', 'imagen')
    ordering = ('fecha_ingreso',)
    search_fields = ('nombre', 'usuario', 'fecha_ingreso', 'jefe', 'rol')
    list_editable = ('fecha_ingreso',
                     'dias_vacaciones_disp', 'jefe', 'rol')
    # list_display_links = ('usuario',)
    list_filter = ('usuario', 'jefe', 'rol', 'area')
    list_per_page = 20
    # exclude = ('dias',)
