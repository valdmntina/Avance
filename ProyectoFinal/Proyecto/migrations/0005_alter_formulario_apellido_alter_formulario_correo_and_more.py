# Generated by Django 5.0.3 on 2024-04-08 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Proyecto', '0004_serpientes_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formulario',
            name='apellido',
            field=models.CharField(max_length=100, verbose_name='Apellido'),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='correo',
            field=models.EmailField(max_length=254, verbose_name='Correo electronico'),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='nombre',
            field=models.CharField(max_length=100, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='telefono',
            field=models.CharField(max_length=10, verbose_name='Telefono'),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='ubicacion',
            field=models.CharField(choices=[(1, 'Amazonas'), (2, 'Vichada'), (3, 'Caquetá'), (4, 'Meta'), (5, 'Guainía'), (6, 'Antioquia'), (7, 'Vaupés'), (8, 'Guaviare'), (9, 'Chocó'), (10, 'Casanare'), (11, 'Nariño'), (12, 'Santander'), (13, 'Cauca'), (14, 'Bolívar'), (15, 'Cordoba'), (16, 'Putumayo'), (17, 'Cundinamarca'), (18, 'Arauca'), (19, 'Tolima'), (20, 'Boyacá'), (21, 'Magdalena'), (22, 'Cesar'), (23, 'Valle del Cauca'), (24, 'Norte de Santander'), (25, 'La Guajira'), (26, 'Huila'), (27, 'Sucre'), (28, 'Caldas'), (29, 'Risaralda'), (30, 'Atlántico'), (31, 'Quindío'), (32, 'Bogotá, D.C')], max_length=100, verbose_name='Ubicacion'),
        ),
    ]
