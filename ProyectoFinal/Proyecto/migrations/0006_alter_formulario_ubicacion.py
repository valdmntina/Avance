# Generated by Django 5.0.3 on 2024-04-08 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Proyecto', '0005_alter_formulario_apellido_alter_formulario_correo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formulario',
            name='ubicacion',
            field=models.CharField(choices=[('Amazonas', 'Amazonas'), ('Vichada', 'Vichada'), ('Caquetá', 'Caquetá'), ('Meta', 'Meta'), ('Guainía', 'Guainía'), ('Antioquia', 'Antioquia'), ('Vaupés', 'Vaupés'), ('Guaviare', 'Guaviare'), ('Chocó', 'Chocó'), ('Casanare', 'Casanare'), ('Nariño', 'Nariño'), ('Santander', 'Santander'), ('Cauca', 'Cauca'), ('Bolívar', 'Bolívar'), ('Cordoba', 'Cordoba'), ('Putumayo', 'Putumayo'), ('Cundinamarca', 'Cundinamarca'), ('Arauca', 'Arauca'), ('Tolima', 'Tolima'), ('Boyacá', 'Boyacá'), ('Magdalena', 'Magdalena'), ('Cesar', 'Cesar'), ('Valle del Cauca', 'Valle del Cauca'), ('Norte de Santander', 'Norte de Santander'), ('La Guajira', 'La Guajira'), ('Huila', 'Huila'), ('Sucre', 'Sucre'), ('Caldas', 'Caldas'), ('Risaralda', 'Risaralda'), ('Atlántico', 'Atlántico'), ('Quindío', 'Quindío'), ('Bogotá, D.C', 'Bogotá, D.C')], max_length=100, verbose_name='Ubicacion'),
        ),
    ]