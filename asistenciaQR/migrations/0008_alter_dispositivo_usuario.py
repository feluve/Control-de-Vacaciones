# Generated by Django 4.1.5 on 2023-07-18 09:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('asistenciaQR', '0007_remove_dispositivo_agente_remove_dispositivo_gpu_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dispositivo',
            name='usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='dispositivo', to=settings.AUTH_USER_MODEL),
        ),
    ]