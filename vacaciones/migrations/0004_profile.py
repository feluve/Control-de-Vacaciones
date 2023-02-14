# Generated by Django 4.1.5 on 2023-02-08 02:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vacaciones', '0003_alter_solicitud_vacaciones_dias_festivos_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='users/image_user.png', upload_to='users/')),
                ('telefono', models.CharField(blank=True, max_length=15, null=True)),
                ('fecha_ingreso', models.DateField(blank=True, null=True)),
                ('area', models.CharField(blank=True, choices=[('Modulos', 'Modulos'), ('Mecanica', 'Mecanica'), ('Laboratorio', 'Laboratorio'), ('Administracion', 'Administracion'), ('Ventas', 'Ventas')], max_length=15, null=True)),
                ('dias_vacaciones_disp', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('jefe', models.CharField(blank=True, choices=[('Javier Gonzalez', 'Javier Gonzalez'), ('Jovani Gonzalez', 'Jovani Gonzalez'), ('Erika Chagolla', 'Erika Gonzalez'), ('Victor Vales', 'Victor Vales'), ('Aldo', 'Aldo'), ('Jorge', 'Jorge'), ('Fransisco', 'Fransisco')], max_length=50, null=True)),
                ('perfil', models.CharField(blank=True, choices=[('Empleado', 'Empleado'), ('Superviso', 'Superviso'), ('Dueño', 'Dueño')], max_length=50, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
