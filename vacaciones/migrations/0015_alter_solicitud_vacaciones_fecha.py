# Generated by Django 4.1.5 on 2023-02-10 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacaciones', '0014_alter_solicitud_vacaciones_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitud_vacaciones',
            name='fecha',
            field=models.DateField(auto_now_add=True),
        ),
    ]
