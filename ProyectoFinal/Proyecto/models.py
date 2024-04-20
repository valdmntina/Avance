from django.db import models

# Create your models here.

#modelo principal de la base de datos que incluye una foto
class Serpientes(models.Model):
    nombre_cientifico = models.CharField(max_length=100)
    nombre_comun = models.CharField(max_length=100)
    habitat = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    foto = models.ImageField(null = True, blank=True)

    def __str__(self):
      return self.nombre_comun
    
#segundo modelo de la base de datos que hereda de serpientes
class Caracteristica(models.Model):
    venenosa = models.BooleanField(default=False) #especifica el valor por defecto si se intenta ingresar un valor vacio
    color_patron = models.CharField(max_length=100)
    alimentacion = models.CharField(max_length=100)
    serpiente = models.OneToOneField(Serpientes, on_delete=models.PROTECT)
   
    def __str__(self):
        return self.venenosa

#formulario basado en modelos
class Formulario(models.Model):
    nombre = models.CharField(max_length=100,
                            #   id="nombre",
                              verbose_name='Nombre',
                              null=False)
    apellido = models.CharField(max_length=100,
                                verbose_name='Apellido')
    telefono = models.CharField(max_length=10,
                                verbose_name='Telefono')
    correo = models.EmailField(verbose_name='Correo electronico')
    
