# Generated by Django 4.1.5 on 2023-04-27 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asistenciaQR', '0002_rename_username_asistenciaqr_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asistenciaqr',
            name='fecha_hora',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]