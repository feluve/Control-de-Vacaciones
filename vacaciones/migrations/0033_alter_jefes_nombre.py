# Generated by Django 4.1.5 on 2023-02-25 16:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vacaciones', '0032_perfil_jefes_delete_sandwich_delete_sauce'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jefes',
            name='nombre',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
