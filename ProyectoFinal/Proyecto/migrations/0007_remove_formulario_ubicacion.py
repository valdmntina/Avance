# Generated by Django 5.0.3 on 2024-04-11 19:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Proyecto', '0006_alter_formulario_ubicacion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formulario',
            name='ubicacion',
        ),
    ]
