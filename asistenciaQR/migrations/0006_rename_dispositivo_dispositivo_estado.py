# Generated by Django 4.1.5 on 2023-07-17 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asistenciaQR', '0005_dispositivo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dispositivo',
            old_name='dispositivo',
            new_name='estado',
        ),
    ]
