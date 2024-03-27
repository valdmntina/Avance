from django.db import models

# Create your models here.

class Serpientes(models.Model):
    nombre_cientifico = models.CharField(max_length=100)
    nombre_comun = models.CharField(max_length=100)
    habitat = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)

class Caracteristica(models.Model):
    venenosa = models.BooleanField(default=False) #especifica el valor por defecto si se intenta ingresar un valor vacio
    color_patron = models.CharField(max_length=100)
    alimentacion = models.CharField(max_length=100)
    serpiente = models.ForeignKey(Serpientes, on_delete=models.PROTECT)
   