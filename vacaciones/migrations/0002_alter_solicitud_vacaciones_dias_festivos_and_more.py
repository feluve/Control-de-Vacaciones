# Generated by Django 4.1.5 on 2023-02-07 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacaciones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitud_vacaciones',
            name='dias_festivos',
            field=models.SmallIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='solicitud_vacaciones',
            name='domingos',
            field=models.SmallIntegerField(blank=True),
        ),
    ]
