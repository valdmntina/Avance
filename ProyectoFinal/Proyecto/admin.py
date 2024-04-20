from django.contrib import admin
from .models import *

class FormularioAdmin(admin.ModelAdmin):
    #aqui define los campos que se van a mostrar en la lista de objetos en el panel de administracion
    list_display = ('nombre', 'apellido', 'telefono')
    #aqui define los campos por los cuales se puede realizar busqueda en el panel de administracion
    search_fields = ('nombre', 'telefono')
    #aqui define los campos por los cuales se puede filtrar la lista de objetos en el panel de administracion
    list_filter = ('nombre', 'apellido')

# Register your models here.
admin.site.register(Serpientes)
admin.site.register(Caracteristica)
admin.site.register(Formulario, FormularioAdmin)