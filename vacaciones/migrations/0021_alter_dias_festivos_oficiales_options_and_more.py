# Generated by Django 4.1.5 on 2023-02-17 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacaciones', '0020_alter_dias_festivos_oficiales_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dias_festivos_oficiales',
            options={'ordering': ['-id'], 'verbose_name': 'Dia festivo oficial', 'verbose_name_plural': 'Dias festivos oficiales'},
        ),
        migrations.AlterModelOptions(
            name='solicitud_vacaciones',
            options={'ordering': ['-id'], 'verbose_name': 'Solicitud de vacaciones', 'verbose_name_plural': 'Solicitudes de vacaciones'},
        ),
        migrations.RemoveField(
            model_name='perfil',
            name='vigencia_dias_vacaciones_disp',
        ),
        migrations.AlterField(
            model_name='perfil',
            name='rol',
            field=models.CharField(blank=True, choices=[('Empleado', 'Empleado'), ('Supervisor', 'Supervisor'), ('Gerente', 'Gerente'), ('RH', 'RH'), ('Direccion', 'Direccion'), ('Dueño', 'Dueño'), ('admin', 'admin')], default='Empleado', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='solicitud_vacaciones',
            name='estado',
            field=models.CharField(choices=[('Pendiente', 'Pendiente'), ('Rechazada', 'Rechazada'), ('Aprobada', 'Aprobada'), ('Cancelada', 'Cancelada')], max_length=50),
        ),
    ]