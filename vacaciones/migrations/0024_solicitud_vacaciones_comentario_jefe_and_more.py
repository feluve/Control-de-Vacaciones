# Generated by Django 4.1.5 on 2023-02-22 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacaciones', '0023_rename_vigencia_dias_vacaciones_disp_perfil_vigencia_dias_vacaciones'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitud_vacaciones',
            name='comentario_jefe',
            field=models.TextField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='solicitud_vacaciones',
            name='comentario_usuario',
            field=models.TextField(blank=True, max_length=250, null=True),
        ),
    ]