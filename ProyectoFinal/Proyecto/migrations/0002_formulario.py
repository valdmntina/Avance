# Generated by Django 5.0.3 on 2024-04-02 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Proyecto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Formulario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=10)),
                ('correo', models.EmailField(max_length=254)),
                ('ubicacion', models.CharField(max_length=100)),
            ],
        ),
    ]
