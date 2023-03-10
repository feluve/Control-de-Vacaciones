# Generated by Django 4.1.5 on 2023-02-09 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacaciones', '0006_alter_perfil_perfil_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='image',
            field=models.ImageField(default='usuarios/image_user.png', upload_to='usuarios/'),
        ),
        migrations.AlterField(
            model_name='solicitud_vacaciones',
            name='estado',
            field=models.CharField(choices=[('Pendiente', 'Pendiente'), ('Rechazada', 'Rechazada'), ('Aprobada', 'Aprobada')], max_length=50),
        ),
    ]
