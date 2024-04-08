from django.db import models

# Create your models here.

options = [
    ['Amazonas', 'Amazonas'],
    ['Vichada', 'Vichada'],
    ['Caquetá', 'Caquetá'],
    ['Meta', 'Meta'],
    ['Guainía', 'Guainía'],
    ['Antioquia', 'Antioquia'],
    ['Vaupés', 'Vaupés'],
    ['Guaviare', 'Guaviare'],
    ['Chocó', 'Chocó'],
    ['Casanare', 'Casanare'],
    ['Nariño', 'Nariño'],
    ['Santander', 'Santander'],
    ['Cauca', 'Cauca'],
    ['Bolívar', 'Bolívar'],
    ['Cordoba', 'Cordoba'],
    ['Putumayo', 'Putumayo'],
    ['Cundinamarca', 'Cundinamarca'],
    ['Arauca', 'Arauca'],
    ['Tolima', 'Tolima'],
    ['Boyacá', 'Boyacá'],
    ['Magdalena', 'Magdalena'],
    ['Cesar', 'Cesar'],
    ['Valle del Cauca', 'Valle del Cauca'],
    ['Norte de Santander', 'Norte de Santander'],
    ['La Guajira', 'La Guajira'],
    ['Huila', 'Huila'],
    ['Sucre', 'Sucre'],
    ['Caldas', 'Caldas'],
    ['Risaralda', 'Risaralda'],
    ['Atlántico', 'Atlántico'],
    ['Quindío', 'Quindío'],
    ['Bogotá, D.C', 'Bogotá, D.C'],
]


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
    ubicacion = models.CharField(choices=options , max_length=100, verbose_name='Ubicacion')