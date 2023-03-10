# Generated by Django 4.1.5 on 2023-02-24 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacaciones', '0029_perfil_semana'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jefes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'verbose_name': 'Jefe',
                'verbose_name_plural': 'Jefes',
                'ordering': ['-id'],
            },
        ),
    ]