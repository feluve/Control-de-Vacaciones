from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.


# --------------------------------------------------------------------

# class Jefes(models.Model):
#     nombre = models.CharField(max_length=50, blank=True, null=True)

#     def __str__(self):
#         return self.nombre

#     class Meta:
#         verbose_name = 'Jefe'
#         verbose_name_plural = 'Jefes'
#         ordering = ['-id']

# --------------------------------------------------------------------


class Perfil(models.Model):

    AREAS = [
        ('Modulos', 'Modulos'),
        ('Mecanica', 'Mecanica'),
        ('Laboratorio', 'Laboratorio'),
        ('Administracion', 'Administracion'),
        ('Ventas', 'Ventas')
    ]

    JEFES = [
        ('Javier Gonzalez', 'Javier Gonzalez'),
        ('Javier Ramirez', 'Javier Ramirez'),
        ('Yovani Gonzalez', 'Yovani Gonzalez'),
        ('Ivan Gonzalez', 'Ivan Gonzalez')
        # ('Erika Chagolla', 'Erika Gonzalez'),
        # ('Victor Valdez', 'Victor Valdez'),
        # ('Aldo Gacía', 'Aldo Gacía'),
        # ('Jorge Hernandez', 'Jorge Hernandez'),
        # ('Fransisco Vargas', 'Fransisco Vargas'),
    ]

    ROL = [
        ('Empleado', 'Empleado'),
        ('Supervisor', 'Supervisor'),
        ('Gerente', 'Gerente'),
        ('RH', 'RH'),
        ('Directivo', 'Directivo'),
        ('admin', 'admin')
    ]
    SEMANA = [
        ('Normal', 'Lunes-Sabado'),
        ('Inglesa', 'Lunes-Viernes')
    ]

    usuario = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='perfil')
    imagen = models.ImageField(
        default='image_user.png', upload_to='users/')
    telefono = models.CharField(max_length=15, null=True, blank=True)
    fecha_ingreso = models.DateField(null=True, blank=True)
    area = models.CharField(max_length=15, null=True,
                            blank=True, choices=AREAS)
    dias_vacaciones_disp = models.SmallIntegerField(
        null=True, blank=True)
    vigencia_dias_vacaciones = models.DateField(null=True, blank=True)
    jefe = models.CharField(max_length=50, null=True,
                            blank=True, choices=JEFES)
    rol = models.CharField(max_length=50, null=True,
                           blank=True, choices=ROL, default="Empleado")
    fecha_nacimiento = models.DateField(null=True, blank=True)
    semana = models.CharField(max_length=50, null=True,
                              blank=True, choices=SEMANA, default="Normal")
    token = models.CharField(max_length=100, null=True, blank=True)
    id_asistencia = models.PositiveSmallIntegerField(null=True, blank=True)

    def __str__(self):
        return self.rol

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'
        ordering = ['-id']


def crear_perfil_usuario(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(usuario=instance)


def guardar_perfil_usuario(sender, instance, **kwargs):
    instance.perfil.save()


post_save.connect(crear_perfil_usuario, sender=User)
post_save.connect(guardar_perfil_usuario, sender=User)


# --------------------------------------------------------------------

class Solicitud_Vacaciones(models.Model):
    ESTADO = [
        ('Pendiente', 'Pendiente'),
        ('Rechazada', 'Rechazada'),
        ('Aprobada', 'Aprobada'),
        ('Cancelada', 'Cancelada')
    ]

    JEFES = [
        ('Javier Gonzalez', 'Javier Gonzalez'),
        ('Javier Ramirez', 'Javier Ramirez'),
        ('Yovani Gonzalez', 'Yovani Gonzalez'),
        ('Ivan Gonzalez', 'Ivan Gonzalez')
        # ('Erika Chagolla', 'Erika Gonzalez'),
        # ('Victor Valdez', 'Victor Valdez'),
        # ('Aldo Gacía', 'Aldo Gacía'),
        # ('Jorge Hernandez', 'Jorge Hernandez'),
        # ('Fransisco Vargas', 'Fransisco Vargas'),
    ]

    usuario = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    fecha = models.DateField(auto_now=False, auto_now_add=True)
    dias = models.SmallIntegerField()
    fecha_inicio = models.DateField(
        auto_now=False, auto_now_add=False)
    fecha_fin = models.DateField(
        auto_now=False, auto_now_add=False)
    jefe = models.CharField(max_length=50, null=True,
                            blank=True, choices=JEFES)
    domingos = models.SmallIntegerField(blank=True, null=True)
    dias_festivos = models.SmallIntegerField(blank=True, null=True)
    estado = models.CharField(
        max_length=50, choices=ESTADO)
    comentario_solicitud = models.TextField(
        max_length=1000, blank=True, null=True)
    comentario_jefe = models.TextField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.usuario

    class Meta:
        verbose_name = 'Solicitud de vacaciones'
        verbose_name_plural = 'Solicitudes de vacaciones'
        ordering = ['-id']


# --------------------------------------------------------------------

class Dias_Festivos_Oficiales(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)
    dia_festivo = models.DateField(
        blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Dia festivo oficial'
        verbose_name_plural = 'Dias festivos oficiales'
        ordering = ['-id']
