from django.db import models

# Create your models here.


class Serpientes(models.Model):
    nombre_cientifico = models.CharField(max_length=100)
    nombre_comun = models.CharField(max_length=100)
    habitat = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    foto = models.ImageField(null = True)

    def __str__(self):
      return self.nombre_comun
    

class Caracteristica(models.Model):
    venenosa = models.BooleanField(default=False) #especifica el valor por defecto si se intenta ingresar un valor vacio
    color_patron = models.CharField(max_length=100)
    alimentacion = models.CharField(max_length=100)
    serpiente = models.OneToOneField(Serpientes, on_delete=models.PROTECT)
   
    def __str__(self):
        return self.venenosa

class Formulario(models.Model):
    nombre = models.CharField(max_length=100,
                              verbose_name='Nombre')
    apellido = models.CharField(max_length=100,
                                verbose_name='Apellido')
    telefono = models.CharField(max_length=10,
                                verbose_name='Telefono')
    correo = models.EmailField(verbose_name='Correo electronico')
