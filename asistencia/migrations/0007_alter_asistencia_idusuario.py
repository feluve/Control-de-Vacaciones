# Generated by Django 4.1.5 on 2023-04-04 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asistencia', '0006_rename_iduser_asistencia_idusuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asistencia',
            name='idUsuario',
            field=models.IntegerField(default=0),
        ),
    ]