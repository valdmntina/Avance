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
    serpiente = models.OneToOneField(Serpientes, on_delete=models.PROTECT)
   
class Formulario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10)
    correo = models.EmailField()
    ubicacion = models.CharField(max_length=100)