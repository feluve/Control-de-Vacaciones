# Generated by Django 4.1.5 on 2023-04-28 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacaciones', '0048_perfil_dispositivo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='dispositivo',
            field=models.CharField(choices=[('No registrado', 'No registrado'), ('Registrado', 'Registrado'), ('Por registrar', 'Por registrar')], default='No registrado', max_length=50),
        ),
    ]
