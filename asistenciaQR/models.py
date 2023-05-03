from django.db import models

# Create your models here.

class AsistenciaQR(models.Model):
    
    usuario = models.CharField(max_length=50, blank=False, null=False)
    fecha_hora = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'AsistenciaQR'
        verbose_name_plural = 'AsistenciasQR'
        ordering = ['-id'] 