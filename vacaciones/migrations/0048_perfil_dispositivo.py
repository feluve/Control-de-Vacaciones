# Generated by Django 4.1.5 on 2023-04-28 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacaciones', '0047_alter_perfil_area_alter_perfil_jefe_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='dispositivo',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
