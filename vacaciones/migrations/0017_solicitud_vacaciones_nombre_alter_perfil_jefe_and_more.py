# Generated by Django 4.1.5 on 2023-02-10 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacaciones', '0016_alter_perfil_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitud_vacaciones',
            name='nombre',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='jefe',
            field=models.CharField(blank=True, choices=[('Javier Gonzalez', 'Javier Gonzalez'), ('Jovani Gonzalez', 'Jovani Gonzalez'), ('Erika Chagolla', 'Erika Gonzalez'), ('Victor Valdez', 'Victor Valdez'), ('Aldo Gacía', 'Aldo Gacía'), ('Jorge Hernandez', 'Jorge Hernandez'), ('Fransisco Vargas', 'Fransisco Vargas')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='rol',
            field=models.CharField(blank=True, choices=[('Empleado', 'Empleado'), ('Supervisor', 'Supervisor'), ('Gerente', 'Gerente'), ('RH', 'RH'), ('Direccion', 'Direccion'), ('Dueño', 'Dueño')], default='Empleado', max_length=50, null=True),
        ),
    ]