# Generated by Django 4.1.5 on 2023-04-27 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asistenciaQR', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='asistenciaqr',
            old_name='username',
            new_name='usuario',
        ),
    ]
