from django.db import models


class Asistencia(models.Model):

    USUARIOS = [
        (3, 'JessicaZuniga'),
        (5, 'AraceliZuniga'),
        (6, 'ErikaChagolla')
    ]

    idUsuario = models.IntegerField(default=0)
    nombre = models.CharField(max_length=100, default='')
    fecha_hora = models.DateTimeField(unique=True)
