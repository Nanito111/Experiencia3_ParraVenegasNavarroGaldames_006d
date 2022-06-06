# Generated by Django 4.0.5 on 2022-06-06 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cuenta',
            fields=[
                ('usuario', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='Usuario')),
                ('nombre', models.CharField(max_length=64, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=64, verbose_name='Apellido')),
                ('correo', models.CharField(max_length=100, verbose_name='Correo')),
                ('password', models.CharField(max_length=50, verbose_name='Contraseña')),
            ],
        ),
    ]
