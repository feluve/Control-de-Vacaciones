from django.db import models
from vacaciones.models import Perfil
from django.contrib.auth.models import User

# Create your models here.

DISPOSITIVO = [
    ('No registrado', 'No registrado'),
    ('Registrado', 'Registrado')
]

class AsistenciaQR(models.Model):
    
    usuario = models.CharField(max_length=50, blank=False, null=False)
    fecha_hora = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'AsistenciaQR'
        verbose_name_plural = 'AsistenciasQR'
        ordering = ['-id'] 

# crear un modelos llamda Dispositivo que este realacionado con el modelo Perfil

class Dispositivo(models.Model):
    
    usuario = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='dispositivo')
    estado = models.CharField(
        max_length=50, choices=DISPOSITIVO, default="No registrado")
    pantalla = models.CharField(max_length=50, blank=True, null=True)
    plataforma = models.CharField(max_length=50, blank=True, null=True)
    nucleos = models.CharField(max_length=50, blank=True, null=True)
    
    class Meta:
        verbose_name = 'Dispositivo'
        verbose_name_plural = 'Dispositivos'
        ordering = ['-id']