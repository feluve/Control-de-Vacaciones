# Generated by Django 4.1.5 on 2023-02-10 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacaciones', '0015_alter_solicitud_vacaciones_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='image',
            field=models.ImageField(default='image_user.png', upload_to='users/'),
        ),
    ]
