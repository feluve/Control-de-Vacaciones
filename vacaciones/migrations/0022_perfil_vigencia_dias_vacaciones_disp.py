# Generated by Django 4.1.5 on 2023-02-21 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacaciones', '0021_alter_dias_festivos_oficiales_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='vigencia_dias_vacaciones_disp',
            field=models.DateField(blank=True, null=True),
        ),
    ]
